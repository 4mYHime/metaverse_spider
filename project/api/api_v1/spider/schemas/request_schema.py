from typing import Union, Any

from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    code: int = Field(default=None, example=200, description="业务响应码")
    message: str = Field(default=None, example="业务提示码", description="业务提示码")
    data: Union[str, dict, Any] = Field(default=None, description="业务信息体")
