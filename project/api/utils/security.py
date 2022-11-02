import time
import json
import pytz
from datetime import datetime, timedelta
from typing import Optional, Union, Any

import jwt
from fastapi import Header
from passlib.context import CryptContext
from pydantic import ValidationError

from api.api_v1.spider.schemas import token_schema
from api.utils import custom_exception
from api.common import response_code
from setting import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(
        subject: Union[str, Any],
        expires_delta: timedelta = None,
) -> str:
    if expires_delta:
        expire = datetime.now(pytz.timezone('PRC')) + expires_delta
    else:
        expire = datetime.now(pytz.timezone('PRC')) + timedelta(
            minutes=60 * 24 * 7
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM).decode()
    return encoded_jwt


def check_jwt_token(
        token: Optional[str] = Header(None)
) -> Union[token_schema.TokenPayload, Any]:
    """
    解析验证token后验证过期时间
    :param token:
    :return:
    """

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY, algorithms=settings.JWT_ALGORITHM
        )
        if payload["exp"] > int(time.mktime(datetime.now(pytz.timezone('PRC')).timetuple())):
            sub = eval(payload["sub"])
            sub.update(dict(token=token))
            payload["sub"] = json.dumps(sub)
            return token_schema.TokenPayload(**payload)
        else:
            raise custom_exception.UserTokenError(code=response_code.TOKEN_INVALID, msg="AccessTokenExpired", data=None)
    except (jwt.exceptions.PyJWTError, jwt.ExpiredSignatureError, ValidationError):
        raise custom_exception.UserTokenError(code=response_code.TOKEN_INVALID, msg="AccessTokenInvalid", data=None)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
