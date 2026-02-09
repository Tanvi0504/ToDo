// ADD TASK
async function addTask() {
    const input = document.getElementById("taskInput");
    const task = input.value.trim();

    if (!task) return;

    const response = await fetch("/add", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ task: task })
    });

    const newTodo = await response.json();

    const li = document.createElement("li");
    li.id = `todo-${newTodo.id}`;
    li.className = newTodo.completed ? "done" : "";

    li.innerHTML = `
        <span>${newTodo.task}</span>
        <button onclick="toggleTask(${newTodo.id})">Toggle</button>
        <button onclick="deleteTask(${newTodo.id})">Delete</button>
    `;

    document.getElementById("todoList").appendChild(li);
    input.value = "";
}


// TOGGLE TASK
async function toggleTask(id) {
    const response = await fetch(`/toggle/${id}`, {
        method: "PUT"
    });

    const updated = await response.json();
    const li = document.getElementById(`todo-${id}`);

    if (updated.completed) {
        li.classList.add("done");
    } else {
        li.classList.remove("done");
    }
}


// DELETE TASK
async function deleteTask(id) {
    await fetch(`/delete/${id}`, {
        method: "DELETE"
    });

    const li = document.getElementById(`todo-${id}`);
    if (li) li.remove();
}
