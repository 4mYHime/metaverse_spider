from typing import Union, Optional, Any, List
from pydantic import BaseModel, Field


class TokenPayload(BaseModel):
    sub: Optional[str] = None


class CRUDBaseSchema(BaseModel):
    code: int = Field(default=0, example=200, description="业务响应码")
    state: bool = Field(default=None, example=False, description="状态")
    data: Union[Any] = Field(default=None, description="业务信息体")
