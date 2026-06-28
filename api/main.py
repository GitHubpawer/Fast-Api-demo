from fastapi import FastAPI

from api.routers.tasks import router as task_router
from api.routers.done import router as done_router

app = FastAPI()

app.include_router(task_router)
app.include_router(done_router)

@app.get("/hello")
async def hello():
    return {"message":"hello world!"}