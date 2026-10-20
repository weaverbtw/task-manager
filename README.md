
# Task Manager

A task management application built with Python, FastAPI, PostgreSQL, and SQLAlchemy. The backend provides a REST API for managing tasks, with JWT authentication and user-specific access controls.

The backend is functional and has been manually tested using FastAPI's interactive API documentation. The React frontend is still a work in progress.

## Features

**Authentication**
- User registration and login
- Password hashing
- JWT-based authentication
- User-specific task access

**Task Management**
- Create, view, rename, and delete tasks
- Mark tasks as complete or incomplete
- Filter tasks by completion status
- Search task names (case-insensitive)
- Prevent duplicate task names within the same user account

## Tech Stack

**Backend:** Python, FastAPI, PostgreSQL, SQLAlchemy, Pydantic, JWT, Passlib/bcrypt

**Frontend (in progress):** React, JavaScript, Vite

## Running the Backend Locally

You'll need Python and PostgreSQL installed. These instructions use Windows PowerShell.

### 1. Clone the repository

```powershell
git clone https://github.com/weaverbtw/task-manager.git
cd task-manager\task-manager-backend
```

### 2. Set up the virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Set up PostgreSQL

Create a database named `task_manager`:

```sql
CREATE DATABASE task_manager;
```

### 4. Configure environment variables

Copy the included environment template:

```powershell
Copy-Item .env.example .env
```

Update `.env` with your database credentials and a secret key:

```env
DATABASE_URL=postgresql+psycopg://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/task_manager
SECRET_KEY=YOUR_GENERATED_SECRET_KEY
```

You can generate a secret key with:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

Keep your `.env` file out of version control.

### 5. Start the server

```powershell
python -m uvicorn main:app --reload
```

The API will run at `http://127.0.0.1:8000`.

FastAPI's interactive API documentation is available at:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

## Trying the API

You can test the backend directly through Swagger UI.

1. Use `POST /users` to register an account.
2. Click **Authorize** and log in with your credentials.
3. Use the task endpoints to create, update, search, and delete tasks.

Each user can only access their own tasks.

## What's Next?

I'm currently working on the React frontend. I also plan to add automated API tests as I continue developing the project.
