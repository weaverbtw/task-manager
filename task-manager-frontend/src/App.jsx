
import {useState} from "react"

function App(){
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [tasks, setTasks] = useState([])
    const [taskName, setTaskName] = useState("")

    async function handleLogin(){
        const formData = new FormData()

        formData.append("username", username)
        formData.append("password", password)

        const response = await fetch(
            "http://127.0.0.1:8000/auth/login",
            {
                method: "POST",

                body: formData
            }
        )

        const data = await response.json()

        localStorage.setItem("access_token", data.access_token)

        console.log(data.access_token)
    }

    async function getTasks(){
        const token = localStorage.getItem("access_token")

        const response = await fetch(
            "http://127.0.0.1:8000/tasks",
            {
                headers: {Authorization: `Bearer ${token}`}
            }
        )

        const data = await response.json()

        setTasks(data)
    }

    async function createTask(){
        const token = localStorage.getItem("access_token")

        const response = await fetch(
            "http://127.0.0.1:8000/tasks",
            {
                method: "POST",

                headers: {"Content-Type": "application/json", Authorization: `Bearer ${token}`},

                body: JSON.stringify({name: taskName})
            }
        )

        const data = await response.json

        console.log(data)

        getTasks()
    }

    async function completeTask(taskId) {
        const token = localStorage.getItem("access_token")

        await fetch(
            `http://127.0.0.1:8000/tasks/complete/${taskId}`,
            {
                method: 'PUT',

                headers: {Authorization: `Bearer ${token}`}
            }
        )

        getTasks()
    }

    async function uncompleteTask(taskId) {
        const token = localStorage.getItem("access_token")

        await fetch(
            `http://127.0.0.1:8000/tasks/uncomplete/${taskId}`,
            {
                method: 'PUT',

                headers: {Authorization: `Bearer ${token}`}
            }
        )

        getTasks()
    }

    async function deleteTask(taskId) {
        const token = localStorage.getItem("access_token")

        await fetch(
            `http://127.0.0.1:8000/tasks/${taskId}`,
            {
                method: "DELETE",

                headers: {Authorization: `Bearer ${token}`}
            }
        )

        getTasks()
    }

    return(
        <div>
            <h1>Login page</h1>

            <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            />

            <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            />

            <input
            type="text"
            placeholder="Task Name"
            value={taskName}
            onChange={(e) => setTaskName(e.target.value)}
            />

            <p>{username}</p>

            <button onClick={handleLogin}>Login</button>
            <button onClick={getTasks}>Get Tasks</button>
            <button onClick={createTask}>Create Task</button>

            {tasks.map((task) => (
                <div key={task.id}>
                    <h3>{task.name}</h3>
                    <p>{task.completed ? "Completed": "Not Completed"}</p>
                    {task.completed ? (<button onClick={() => uncompleteTask(task.id)}>Uncomplete</button>):
                                      (<button onClick={() => completeTask(task.id)}>Complete</button>)
                    }
                    <button onClick={() => deleteTask(task.id)}>Delete</button>
                </div>
            ))}

        </div>
    )
}

export default App
