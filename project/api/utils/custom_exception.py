"""

自定义异常

"""


class UserTokenError(Exception):
    def __init__(self, code: int = 2001, msg: str = "用户认证异常", data=None):
        self.code = code
        self.msg = msg
        self.data = data


class UserNotFound(Exception):
    def __init__(self, err_desc: str = "没有此用户"):
        self.err_desc = err_desc


class PostParamsError(Exception):
    def __init__(self, err_desc: str = "POST请求参数错误"):
        self.err_desc = err_desc


class GetParamsError(Exception):
    def __init__(self, err_desc: str = "GET请求参数错误"):
        self.err_desc = err_desc

