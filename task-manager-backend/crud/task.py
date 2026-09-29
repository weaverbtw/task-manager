
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.task import Task

def get_all_tasks(db: Session, current_user_id: int, completed: bool | None = None):
    query = db.query(Task).filter(Task.user_id == current_user_id)

    if completed is not None:
        query = query.filter(Task.completed.is_(completed))

    return query.all()

def search_tasks(db: Session, current_user_id: int, name: str):
    query = db.query(Task).filter(Task.user_id == current_user_id)

    return query.filter(Task.name.ilike(f"%{name}%")).all()

def get_task_by_id(db: Session, current_user_id: int, task_id: int):
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

def create_task(db: Session, current_user_id: int, task_name: str):
    existing_task = db.query(Task).filter(Task.name == task_name).first()

    if existing_task:
        raise HTTPException(status_code=400, detail="Task already exists")

    new_task = Task(name=task_name, user_id=current_user_id)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def complete_task(db: Session, current_user_id: int, task_id: int):
    task = get_task_by_id(db, current_user_id, task_id)

    if task.completed:
        raise HTTPException(status_code=400, detail="Task already completed")

    task.completed = True

    db.commit()
    db.refresh(task)

    return task

def uncomplete_task(db: Session, current_user_id: int, task_id: int):
    task = get_task_by_id(db, current_user_id, task_id)

    if not task.completed:
        raise HTTPException(status_code=400, detail="Task never completed")

    task.completed = False

    db.commit()
    db.refresh(task)

    return task

def update_task(db: Session, current_user_id: int, task_id: int, task_name: str):
    existing_task = db.query(Task).filter(Task.name == task_name, Task.id != task_id, Task.user_id == current_user_id).first()

    if existing_task:
        raise HTTPException(status_code=400, detail="Task with that name already exists")

    task = get_task_by_id(db, current_user_id, task_id)

    task.name = task_name

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, current_user_id: int, task_id: int):
    task = get_task_by_id(db, current_user_id, task_id)

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}
