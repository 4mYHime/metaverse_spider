# 创建app
from api import create_app
app = create_app()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app="main:app", host="0.0.0.0", port=20018, reload=True, workers=2, log_level="debug")
