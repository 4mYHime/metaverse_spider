# windows10
1. celery
   - `celery -A celery_app.celery worker -l info --loglevel=info --pool=solo`
2. snowflake
   - `snowflake_start_server --address=127.0.0.1 --port=6001 --dc=1 --worker=1`
3. redis
   - `.\redis-server.exe .\redis.windows.conf`


# deploy in single server
1. build docker image
   - `docker build -t xx/xx:xx .`
   - `xx/xx:xx` 对应 `docker-compose.yml` 中使用到改镜像的 `service.image` 字段
2. update `pip` version
   - `pip install --upgrade pip`
3. install `docker-compose`
   - `pip install docker-compose`
4. run container
   - `docker-compose -p xxx up -d `
   - `xxx` 指定一个项目名称，specify a project name

# 后期项目更新重启容器
1. 拉取代码
   - `git pull`
2. 重建容器
   - `docker-compose -p xxx up -d`
3. 重启
   - `docker-compose -p xxx restart`