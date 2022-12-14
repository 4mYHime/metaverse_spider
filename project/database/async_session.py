from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

try:
    from setting.settings import configure

    # configure = json.loads(os.environ.get('metaverse_spider_envfile'))
    MYSQL_DIALECT = configure['mysql']['dialect']
    ASYNC_MYSQL_DRIVER = configure['mysql']['async_driver']
    MYSQL_USERNAME = configure['mysql']['username']
    MYSQL_PASSWORD = configure['mysql']['password']
    MYSQL_HOST = configure['mysql']['host']
    MYSQL_PORT = configure['mysql']['port']
    MYSQL_DATABASE = configure['mysql']['database']
except Exception as e:
    raise Exception("请检查环境配置是否正确")

ASYNC_MYSQL_SQLALCHEMY_DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(
    MYSQL_DIALECT, ASYNC_MYSQL_DRIVER, MYSQL_USERNAME, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DATABASE)

# 数据库引擎，也是连接池
async_engine = create_async_engine(ASYNC_MYSQL_SQLALCHEMY_DB_URI,
                                   pool_size=200,
                                   pool_recycle=120,
                                   max_overflow=200)
# 创建session元类
async_session_local = sessionmaker(
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
    bind=async_engine)


# session 生成器，作为fastapi的depends选项
async def db_session() -> AsyncSession:
    async with async_session_local() as session:
        yield session
