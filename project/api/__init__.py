import datetime
import json
import logging
import os
from typing import List

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, ValidationError
from starlette.middleware.cors import CORSMiddleware

from api.api_v1.api import api_v1_router
from api.utils import response_code
from api.utils.custom_exception import PostParamsError, UserTokenError, UserNotFound, GetParamsError
from database.models import Announcement18Art, Announcement42verse, AnnouncementIbox, AnnouncementLingjingsj, \
    AnnouncementShuzimart, AnnouncementTheone
from database.sync_session import get_dbs
from setting import settings
from spider import *


def create_app() -> FastAPI:
    app = FastAPI(openapi_url="/metaverse_spider/openapi.json",
                  docs_url="/metaverse_spider/swagger-ui.html",
                  redoc_url="/metaverse_spider/redoc.html", )
    # 跨域设置
    register_cors(app)

    # 注册路由
    register_router(app)

    # 注册捕获全局异常
    register_exception(app)

    # 请求拦截
    register_middleware(app)

    # 注册配置文件
    register_configure(app)

    return app


def create_app_with_task() -> FastAPI:
    app = FastAPI(openapi_url="/metaverse_spider/openapi.json",
                  docs_url="/metaverse_spider/swagger-ui.html",
                  redoc_url="/metaverse_spider/redoc.html", )
    # 跨域设置
    register_cors(app)

    # 注册路由
    register_router(app)

    # 注册捕获全局异常
    register_exception(app)

    # 请求拦截
    register_middleware(app)

    # 加载数据库定时任务
    register_cron(app)

    # 注册配置文件
    register_configure(app)

    return app

def register_router(app: FastAPI) -> None:
    """
    注册路由
    :param app:
    :return:
    """
    # 项目API

    app.include_router(
        api_v1_router,
        prefix="/metaverse_spider"  # 前缀
    )


def register_cors(app: FastAPI) -> None:
    """
    支持跨域
    :param app:
    :return:
    """
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["http://localhost.tiangolo.com",
                           "https://localhost.tiangolo.com",
                           "http://localhost",
                           "http://localhost:8080",
                           "http://localhost:8000"],
            allow_credentials=True,  # Credentials (Authorization headers, Cookies, etc)
            allow_methods=["*"],  # Specific HTTP methods (POST, PUT) or all of them with the wildcard "*".
            allow_headers=["*"],  # Specific HTTP headers or all of them with the wildcard "*".
        )


def register_exception(app: FastAPI):
    """
    全局异常捕获
    注意 别手误多敲一个s
    exception_handler
    exception_handlers
    两者有区别
        如果只捕获一个异常 启动会报错
        @exception_handlers(UserNotFound)
    TypeError: 'dict' object is not callable
    :param app:
    :return:
    """

    # 自定义异常 捕获
    @app.exception_handler(UserNotFound)
    async def user_not_found_exception_handler(request: Request, exc: UserNotFound):
        """
        用户认证未找到
        :param request:
        :param exc:
        :return:
        """
        return response_code.resp_500(message=exc.err_desc)

    @app.exception_handler(UserTokenError)
    async def user_token_exception_handler(request: Request, exc: UserTokenError):
        """
        用户token异常
        :param request:
        :param exc:
        :return:
        """
        return response_code.resp_200(code=exc.code, msg=exc.msg, data=exc.data)

    @app.exception_handler(PostParamsError)
    async def query_params_exception_handler(request: Request, exc: PostParamsError):
        """
        内部查询操作时，其他参数异常
        :param request:
        :param exc:
        :return:
        """
        return response_code.resp_400(message=exc.err_desc)

    @app.exception_handler(ValidationError)
    async def inner_validation_exception_handler(request: Request, exc: ValidationError):
        """
        内部参数验证异常
        :param request:
        :param exc:
        :return:
        """
        return response_code.resp_500(message=exc.errors())

    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        请求参数验证异常
        :param request:
        :param exc:
        :return:
        """
        return response_code.resp_422(message=exc.errors())

    # 捕获全部异常
    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        """
        全局所有异常
        :param request:
        :param exc:
        :return:
        """
        return response_code.resp_500(message="Server Error")

    # 本项目新建
    @app.exception_handler(GetParamsError)
    async def get_query_params_exception_handler(request: Request, exc: GetParamsError):
        """
        内部查询操作时，其他参数异常
        :param request:
        :param exc:
        :return:
        """
        return response_code.resp_400(message=exc.err_desc)


def register_middleware(app: FastAPI) -> None:
    """
    请求响应拦截 hook
    https://fastapi.tiangolo.com/tutorial/middleware/
    :param app:
    :return:
    """

    @app.middleware("http")
    async def logger_request(request: Request, call_next):
        response = await call_next(request)
        return response


def register_cron(app: FastAPI) -> None:
    from apscheduler.schedulers.asyncio import AsyncIOScheduler
    scheduler = AsyncIOScheduler(timezone="Asia/Shanghai")
    # cron 定时 hour/minute/second
    # interval 间隔
    # 每5分钟 自动抓取最新数据并更新

    scheduler.add_job(spider_18art, 'cron', minute="*/5")
    scheduler.add_job(spider_42verse, 'cron', minute="*/5")
    scheduler.add_job(spider_ibox, 'cron', minute="*/5")
    scheduler.add_job(spider_lingjingsj, 'cron', minute="*/5")
    scheduler.add_job(spider_shuzimart, 'cron', minute="*/5")
    scheduler.add_job(spider_theone, 'cron', minute="*/5")
    try:
        scheduler.start()
    except Exception as e:
        scheduler.shutdown()


def register_configure(app: FastAPI) -> None:
    """
        把配置文件挂载到app对象上面
        :param app:
        :return:
    """

    @app.on_event('startup')
    async def startup_event():
        try:
            from setting.settings import configure
            app.state.configure = configure
            # app.state.configure = json.loads(os.environ.get('metaverse_spider_envfile'))
        except Exception as e:
            raise Exception("请检查环境配置是否正确")


def spider_18art():
    # 执行一次抓取各平台最新数据A
    # A与数据库内容B进行比对
    # 将新的保存至数据库
    with get_dbs() as session:
        content = _18art_announcement_catch()
        if not content['state']:
            logging.warning(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                            f"platform: 18art"
                            f"message: {content['msg']}")
        else:
            content_ids = []
            for i in content['data']['noticeList']:
                for j in i['list']:
                    try:
                        if j['id'] and isinstance(j['id'], str):
                            content_ids.append(j['id'])
                    except Exception as e:
                        continue
            content_18art_ids = list(set(content_ids))
            db_ids: List[Announcement18Art.id] = session.query(Announcement18Art.id).filter(
                Announcement18Art.is_delete == 0
            ).all()
            if len(content_18art_ids) > len(db_ids):
                new_content_ids = list(
                    set(content_18art_ids).difference(set(db_ids))
                )
                for new_id in new_content_ids:
                    for i in content['data']['noticeList']:
                        for j in i['list']:
                            if j['id'] == new_id:
                                try:
                                    session.add(
                                        Announcement18Art(
                                            id=j['id'],
                                            type=j['classId'],
                                            type_name=j['className'],
                                            title=j['title'],
                                            cover="https://file.18art.art" + j['coverImg'],
                                            content=j,
                                            content_type="object",
                                            create_time=datetime.datetime.fromtimestamp(j['time'] / 1000)
                                        )
                                    )
                                except Exception as e:
                                    continue


def spider_42verse():
    # 执行一次抓取各平台最新数据A
    # A与数据库内容B进行比对
    # 将新的保存至数据库
    with get_dbs() as session:
        content = _42verse_announcement_catch()
        if not content['state']:
            logging.warning(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                            f"platform: 42verse"
                            f"message: {content['msg']}")
        else:
            content_ids = []
            content_data = []
            for i in content['data'].values():
                for j in i:
                    content_data.append(j)
            content['data'] = content_data
            for i in content['data']:
                try:
                    if i['id'] and isinstance(i['id'], int):
                        content_ids.append(i['id'])
                except Exception as e:
                    continue
            content_42verse_ids = list(set(content_ids))
            db_ids: List[Announcement42verse.id] = session.query(Announcement42verse.id).filter(
                Announcement42verse.is_delete == 0
            ).all()
            if len(content_42verse_ids) > len(db_ids):
                new_content_ids = list(
                    set(content_42verse_ids).difference(set(db_ids))
                )
                for new_id in new_content_ids:
                    for j in content['data']:
                        if j['id'] == new_id:
                            try:
                                session.add(
                                    Announcement42verse(
                                        id=j['id'],
                                        type_name=j['title'].split('｜')[0],
                                        title=j['title'],
                                        content=j,
                                        content_type="object",
                                        create_time=datetime.datetime.strptime(j["createTime"], "%Y-%m-%d")
                                    )
                                )
                            except Exception as e:
                                continue


def spider_ibox():
    # 执行一次抓取各平台最新数据A
    # A与数据库内容B进行比对
    # 将新的保存至数据库
    with get_dbs() as session:
        content = _ibox_announcement_catch()
        if not content['state']:
            logging.warning(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                            f"platform: ibox"
                            f"message: {content['msg']}")
        else:
            content_ids = []
            content_data = []
            for i in content['data']['allList']:
                try:
                    if i['id'] and isinstance(i['id'], int):
                        content_ids.append(i['id'])
                except Exception as e:
                    continue
            content_ibox_ids = list(set(content_ids))
            db_ids: List[AnnouncementIbox.id] = session.query(AnnouncementIbox.id).filter(
                AnnouncementIbox.is_delete == 0
            ).all()
            if len(content_ibox_ids) > len(db_ids):
                new_content_ids = list(
                    set(content_ibox_ids).difference(set(db_ids))
                )
                for new_id in new_content_ids:
                    for j in content['data']['allList']:
                        if j['id'] == new_id:
                            try:
                                session.add(
                                    AnnouncementIbox(
                                        id=j['id'],
                                        type=j['noticeClassId'],
                                        type_name=j['className'],
                                        title=j['noticeName'],
                                        content=j,
                                        content_type="object",
                                        create_time=datetime.datetime.fromtimestamp(j['noticeTime'] / 1000)
                                    )
                                )
                            except Exception as e:
                                continue


def spider_lingjingsj():
    # 执行一次抓取各平台最新数据A
    # A与数据库内容B进行比对
    # 将新的保存至数据库
    with get_dbs() as session:
        content = _lingjingsj_announcement_catch()
        if not content['state']:
            logging.warning(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                            f"platform: lingjingsj"
                            f"message: {content['msg']}")
        else:
            content_ids = []
            content_data = []
            for i in content['data'].values():
                for j in i:
                    content_data.append(j)
            content['data'] = content_data
            for i in content['data']:
                try:
                    if i['id'] and isinstance(i['id'], int):
                        content_ids.append(i['id'])
                except Exception as e:
                    continue
            content_ids = list(set(content_ids))
            db_ids: List[AnnouncementLingjingsj.id] = session.query(AnnouncementLingjingsj.id).filter(
                AnnouncementLingjingsj.is_delete == 0
            ).all()
            if len(content_ids) > len(db_ids):
                new_content_ids = list(
                    set(content_ids).difference(set(db_ids))
                )
                for new_id in new_content_ids:
                    for j in content['data']:
                        if j['id'] == new_id:
                            try:
                                session.add(
                                    AnnouncementLingjingsj(
                                        id=j['id'],
                                        type_name=j['tag'],
                                        title=j['title'],
                                        content=j,
                                        content_type="object",
                                        create_time=datetime.datetime.strptime(j["create_time"], "%Y-%m-%d %H:%M:%S")
                                    )
                                )
                            except Exception as e:
                                continue


def spider_shuzimart():
    # 执行一次抓取各平台最新数据A
    # A与数据库内容B进行比对
    # 将新的保存至数据库
    with get_dbs() as session:
        content = _shuzimart_announcement_catch()
        if not content['state']:
            logging.warning(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                            f"platform: shuzimart"
                            f"message: {content['msg']}")
        else:
            content_ids = []
            content_data = []
            for i in content['data'].values():
                for j in i:
                    content_data.append(j)
            content['data'] = content_data
            for i in content['data']:
                try:
                    if i['article_id'] and isinstance(i['article_id'], int):
                        content_ids.append(i['article_id'])
                except Exception as e:
                    continue
            content_ids = list(set(content_ids))
            db_ids: List[AnnouncementShuzimart.id] = session.query(AnnouncementShuzimart.id).filter(
                AnnouncementShuzimart.is_delete == 0
            ).all()
            if len(content_ids) > len(db_ids):
                new_content_ids = list(
                    set(content_ids).difference(set(db_ids))
                )
                for new_id in new_content_ids:
                    for j in content['data']:
                        if j['article_id'] == new_id:
                            try:
                                session.add(
                                    AnnouncementShuzimart(
                                        id=j['article_id'],
                                        type=j['category_id'],
                                        type_name=j['category']['name'],
                                        title=j['article_title'],
                                        content=j,
                                        content_type="object",
                                        create_time=datetime.datetime.strptime(j["view_time"], "%Y-%m-%d")
                                    )
                                )
                            except Exception as e:
                                continue


def spider_theone():
    # 执行一次抓取各平台最新数据A
    # A与数据库内容B进行比对
    # 将新的保存至数据库
    with get_dbs() as session:
        content = _theone_announcement_catch()
        if not content['state']:
            logging.warning(f"time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                            f"platform: theone"
                            f"message: {content['msg']}")
        else:
            content_ids = []
            content_data = []
            for i in content['data'].values():
                for j in i:
                    content_data.append(j)
            content['data'] = content_data
            for i in content['data']:
                try:
                    if i['uuid'] and isinstance(i['uuid'], str):
                        content_ids.append(i['uuid'])
                except Exception as e:
                    continue
            content_ids = list(set(content_ids))
            db_ids: List[AnnouncementTheone.id] = session.query(AnnouncementTheone.id).filter(
                AnnouncementTheone.is_delete == 0
            ).all()
            if len(content_ids) > len(db_ids):
                new_content_ids = list(
                    set(content_ids).difference(set(db_ids))
                )
                for new_id in new_content_ids:
                    for j in content['data']:
                        if j['uuid'] == new_id:
                            try:
                                session.add(
                                    AnnouncementTheone(
                                        id=j['uuid'],
                                        type_name='平台通知',
                                        title=j['name'],
                                        cover=j['cover'],
                                        content=j,
                                        content_type="object",
                                        create_time=datetime.datetime.strptime(j["releaseTime"], "%Y/%m/%d %H:%M:%S")
                                    )
                                )
                            except Exception as e:
                                continue
