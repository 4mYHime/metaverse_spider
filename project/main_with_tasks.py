# 创建app
from api import create_app_with_task
app = create_app_with_task()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main_with_tasks:app", host="0.0.0.0", port=20015, reload=True, debug=True, workers=1, log_level="debug")
