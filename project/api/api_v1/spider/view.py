# coding=utf-8

from fastapi import APIRouter, Request

from api.api_v1.spider.crud import crud as authentic_crud
from api.api_v1.spider.schemas import request_schema, response_schema

router = APIRouter()


@router.post(path='/api/spider/login/apple', summary="",
             response_model=response_schema.BaseSchema)
async def login_via_apple_id(*, request: Request, params: request_schema.BaseSchema):
    authentic_resp_1 = await authentic_crud.login_via_apple(params=params, request=request)
    if authentic_resp_1.state:
        return response_schema.BaseSchema(code=200, data=authentic_resp_1.data)
    return response_schema.BaseSchema(code=authentic_resp_1.code, message=authentic_resp_1.data["message"], data={})
