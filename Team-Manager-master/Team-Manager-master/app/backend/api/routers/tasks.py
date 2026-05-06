from fastapi import APIRouter
from app.backend.database import cr, conn
from .. import schemas

router = APIRouter(tags=["Tasks"], prefix="/task")


@router.get("/all", response_model=list[schemas.TaskReturn])
def get_all_tasks():
    return [
        {"id": 1, "title": "Build API", "status": "Completed"},
        {"id": 2, "title": "Fix bugs", "status": "Pending"}
    ]

    cr.execute("""SELECT * FROM tasks""")
    tasks = cr.fetchall()
    return tasks
