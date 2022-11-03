from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


try:
    # configure = json.loads(os.environ.get('metaverse_spider_envfile'))
    from setting.settings import configure
    MYSQL_DIALECT = configure['mysql']['dialect']
    SYNC_MYSQL_DRIVER = configure['mysql']['sync_driver']
    MYSQL_USERNAME = configure['mysql']['username']
    MYSQL_PASSWORD = configure['mysql']['password']
    MYSQL_HOST = configure['mysql']['host']
    MYSQL_PORT = configure['mysql']['port']
    MYSQL_DATABASE = configure['mysql']['database']
except Exception as e:
    raise Exception("请检查环境配置是否正确")

MYSQL_SQLALCHEMY_DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(
    MYSQL_DIALECT, SYNC_MYSQL_DRIVER, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE)

engine = create_engine(MYSQL_SQLALCHEMY_DB_URI,
                       pool_size=200,
                       pool_recycle=120,
                       max_overflow=200)

Session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


# 实例化session
def get_session():
    return Session()


@contextmanager
def get_dbs() -> Generator:
    session = get_session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
