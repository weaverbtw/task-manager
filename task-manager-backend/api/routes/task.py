
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud.task as crud
from database import get_db
from schemas.task import TaskCreate, TaskUpdate, TaskResponse
from dependancies.auth import get_current_user
from models.user import User

router = APIRouter(tags=["Task"])

@router.get("/")
def home():
    return {"message": "Task Manager Online"}

@router.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks(completed: bool | None = None,
                  db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    return crud.get_all_tasks(db, current_user.id, completed)

@router.get("/tasks/search", response_model=list[TaskResponse])
def search_tasks(name: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.search_tasks(db, current_user.id, name)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task_by_id(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.get_task_by_id(db, current_user.id, task_id)

@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.create_task(db, current_user.id, task.name)

@router.put("/tasks/complete/{task_id}", response_model=TaskResponse)
def complete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.complete_task(db, current_user.id, task_id)

@router.put("/tasks/uncomplete/{task_id}", response_model=TaskResponse)
def uncomplete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.uncomplete_task(db, current_user.id, task_id)

@router.put("/tasks/update/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.update_task(db, current_user.id, task_id, task.name)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return crud.delete_task(db, current_user.id, task_id)