# coding=utf-8

from fastapi import APIRouter, Request, Query

from api.api_v1.spider.crud import crud as spider_crud
from api.api_v1.spider.schemas import response_schema

router = APIRouter()


@router.get(path='/announcement', summary="18art",
            response_model=response_schema.BaseSchema)
async def get_announcement(*,
                           request: Request,
                           platform: int = Query(default=None, description=f"平台\n"
                                                                           f"1-18art\n"
                                                                           f"2-42verse\n"
                                                                           f"3-ibox\n"
                                                                           f"4-lingjingsj\n"
                                                                           f"5-shuzimart\n"
                                                                           f"6-theone"),
                           ):
    spider_resp_1 = await spider_crud.get_announcement(platform=platform, request=request)
    if spider_resp_1.state:
        return response_schema.BaseSchema(code=200, data=spider_resp_1.data)
    return response_schema.BaseSchema(code=spider_resp_1.code, message=spider_resp_1.data["message"], data={})
