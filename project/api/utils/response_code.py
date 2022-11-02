from typing import Union, Any

from fastapi import status
from fastapi.responses import JSONResponse, Response  # , ORJSONResponse


def resp_200(*, code: int, data: Union[list, dict, str, Any] = None, msg: str = "Success"):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': code,
            'msg': msg,
            'data': data,
        }
    )


def resp_400(*, data: str = None, message: str = "BAD REQUEST") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'message': message,
        }
    )


def resp_403(*, data: str = None, message: str = "Forbidden") -> Response:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            'message': message,
        }
    )


def resp_404(*, data: str = None, message: str = "Page Not Found") -> Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            'message': message,
        }
    )


def resp_422(*, data: str = None, message: Union[list, dict, str] = "UNPROCESSABLE_ENTITY") -> Response:
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            'message': message,
        }
    )


def resp_500(*, data: str = None, message: Union[list, dict, str] = "Server Internal Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            'message': message,
        }
    )
