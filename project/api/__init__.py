import json
import os

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError, ValidationError
from starlette.middleware.cors import CORSMiddleware

from api.api_v1.api import api_v1_router
from api.utils import response_code
from api.utils.custom_exception import PostParamsError, UserTokenError, UserNotFound, GetParamsError
from database.async_session import get_redis_pool
from setting import settings


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


def register_redis(app: FastAPI) -> None:
    """
        把redis挂载到app对象上面
        :param app:
        :return:
    """

    @app.on_event('startup')
    async def startup_event():
        app.state.redis = await get_redis_pool()

    @app.on_event('shutdown')
    async def shutdown_event():
        app.state.redis.close()
        await app.state.redis.wait_closed()


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

    try:
        scheduler.start()
    except Exception as e:
        # print(e)
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
            app.state.configure = json.loads(os.environ.get('metaverse_spider_envfile'))
        except Exception as e:
            raise Exception("请检查环境配置是否正确")
