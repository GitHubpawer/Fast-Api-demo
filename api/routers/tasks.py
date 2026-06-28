from fastapi import APIRouter

router = APIRouter()

@router.get("/tasks")
async def list_tasks():
    return {"message":"task list"}

@router.post("/tasks")
async def create_task():
    return {"message":"created"}

@router.put("/tasks/{task_id}")
async def update_task(task_id: int):
    return {"task_id": task_id}

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    return {"task_id": task_id}