from fastapi import APIRouter
from taskiq import TaskiqResult
from models.tasks import  TaskResults, TasksResultsRequest
from task_runner import broker

router = APIRouter()


async def check_task_status(task: TasksResultsRequest) -> bool:
    is_ready: bool = await broker.result_backend.is_result_ready(task.task_id)
    if is_ready:
        result: TaskiqResult[TaskResults] = (
            await broker.result_backend.get_result(task.task_id)
        )
        result.result.task_id = task.task_id
        result.result.ready = True
        result.result.poll_count = task.poll_count
        result.result.execution_time = result.execution_time
        return result.result
    else:
        return TaskResults(task_id=task.task_id, 
                           poll_count=task.poll_count,
                           ready=False)
    

@router.get("/tasks_results")
async def get_task_status(req: list[TasksResultsRequest]) -> list[TaskResults]:
    task_statuses: list[TaskResults] = []
    for task in req:
        result = await check_task_status(task)
        task_statuses.append(result)
    return task_statuses