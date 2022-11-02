from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    SECRET_KEY: str = "(-ASp+_)-Ulhw0848hnvVG-iqKyJSD&*&^-H3C9mqEqSl8KN-YRzRE"

    JWT_ALGORITHM: str = "HS256"

    BACKEND_CORS_ORIGINS: List[str] = ['*']
    ENCODING_STR = "E5FCDG3HQA4B1NOPIJ2RSTUV67MWX89KLYZ"


settings = Settings()
