
# Task Manager

A task management application built with **Python, FastAPI, PostgreSQL, and SQLAlchemy**. Its REST API supports user registration, JWT-based login, and task management with user-specific access controls.

**Project status:** The backend is functional and has been manually tested locally using FastAPI's interactive API documentation. The React frontend is still in development.

## Features

### Authentication and Authorization

- Register users and log in with a username and password
- Hash passwords before storing them
- Authenticate requests using JSON Web Tokens (JWTs)
- Restrict task retrieval, updates, and deletion to the authenticated task owner

### Task Management

- Create, view, rename, and delete tasks
- Mark tasks as complete or incomplete
- Filter tasks by completion status
- Search task names (case-insensitive)
- Prevent duplicate task names within the same user account

## Tech Stack

**Backend**
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT authentication (python-jose)
- Passlib and bcrypt for password hashing

**Frontend — in development**
- React
- JavaScript
- Vite

## Project Structure

```text
task-manager/
├── task-manager-backend/
│   ├── api/routes/       # Authentication, user, and task endpoints
│   ├── core/             # Configuration and security utilities
│   ├── crud/             # Database operations
│   ├── dependancies/     # Authentication dependency
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic request/response schemas
│   ├── .env.example      # Example environment configuration
│   ├── database.py       # Database engine and session setup
│   ├── main.py           # FastAPI application
│   └── requirements.txt  # Python dependencies
├── task-manager-frontend/ # React/Vite application (unfinished)
└── README.md
```

## Prerequisites

To run the **backend** locally, you'll need:

- Python (3.13 was used during development)
- PostgreSQL
- Git

To work on the **unfinished frontend**, you'll also need Node.js and npm.

A code editor such as VS Code and a database tool such as pgAdmin 4 are optional.

## Running the Backend Locally

The following commands use **Windows PowerShell**.

### 1. Clone the repository

```powershell
git clone https://github.com/weaverbtw/task-manager.git
cd task-manager\task-manager-backend
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Create a PostgreSQL database

With PostgreSQL running, use pgAdmin 4 or a PostgreSQL SQL client to execute:

```sql
CREATE DATABASE task_manager;
```

You can choose another database name, but it must match the connection string in your environment configuration.

### 5. Configure environment variables

Create a local `.env` file from the included template:

```powershell
Copy-Item .env.example .env
```

Edit `.env` with your own PostgreSQL credentials and secret key:

```dotenv
DATABASE_URL=postgresql+psycopg://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/task_manager
SECRET_KEY=YOUR_GENERATED_SECRET_KEY
```

Generate a random secret key with:

```powershell
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the resulting value into `SECRET_KEY`.

**Security:** Do not commit `.env`, database passwords, access tokens, or secret keys to GitHub. The repository includes `.env.example` for safe configuration sharing.

### 6. Start the FastAPI server

From the `task-manager-backend` directory, run:

```powershell
python -m uvicorn main:app --reload
```

On startup, SQLAlchemy creates the application's database tables if they do not already exist.

The API runs locally at **http://127.0.0.1:8000**. Open **http://127.0.0.1:8000/docs** for Swagger UI or **http://127.0.0.1:8000/redoc** for ReDoc.

## Trying the API

You can use Swagger UI to interact with the API without installing a separate API client.

1. Open `http://127.0.0.1:8000/docs`.
2. Use **POST `/users`** to register a user.
3. Click **Authorize** and enter that user's username and password. Swagger UI obtains a JWT through the login endpoint.
4. Use **POST `/tasks`** to create a task, such as:

   ```json
   {
     "name": "Finish project README"
   }
   ```

5. Try listing, searching, completing, renaming, or deleting your tasks.

The protected task endpoints require an authenticated user.

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | API status message |
| `POST` | `/users` | Register a user |
| `POST` | `/auth/login` | Log in and obtain a JWT |
| `GET` | `/tasks` | List the authenticated user's tasks; optionally filter with `?completed=true` or `?completed=false` |
| `GET` | `/tasks/search?name=...` | Search the authenticated user's task names |
| `GET` | `/tasks/{task_id}` | Retrieve a task by ID |
| `POST` | `/tasks` | Create a task |
| `PUT` | `/tasks/complete/{task_id}` | Mark a task as complete |
| `PUT` | `/tasks/uncomplete/{task_id}` | Mark a task as incomplete |
| `PUT` | `/tasks/update/{task_id}` | Rename a task |
| `DELETE` | `/tasks/{task_id}` | Delete a task |

Except for registration, login, and the root status endpoint, these routes require JWT authentication. Task operations are scoped to the authenticated user.

## Frontend Status

The repository includes a **React/Vite frontend that is still in development**. It is not yet a finished user interface for the backend.

To run its development server, open another terminal from the repository root and run:

```powershell
cd task-manager-frontend
npm install
npm run dev
```

The Vite development server generally opens at `http://localhost:5173`. Frontend functionality is incomplete.

## Current Scope

This project is focused on building and understanding a REST API with database persistence, authentication, and user-specific authorization. The backend has been manually tested locally; comprehensive automated API tests and a completed frontend are future improvements.
