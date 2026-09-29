
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
import models.task
import models.user
from api.routes.auth import router as auth_router
from api.routes.task import router as task_router
from api.routes.user import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

app.include_router(auth_router)
app.include_router(task_router)
app.include_router(user_router)