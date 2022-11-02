from typing import Union, Any

from pydantic import BaseModel, Field


class CRUDBaseSchema(BaseModel):
    state: bool = Field(default=None, example=False, description="状态")
    data: Union[Any] = Field(default=None, description="业务信息体")
