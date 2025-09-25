const API_URL = "http://127.0.0.1:8000";

// ========== ЗАДАЧИ ==========
async function loadTasks() {
    const res = await fetch(`${API_URL}/tasks`);
    const data = await res.json();
    const ul = document.getElementById("tasks");
    if (!ul) return; // если не на index.html — выходим
    ul.innerHTML = "";
    data.forEach(task => {
        const li = document.createElement("li");
        li.textContent = `${task.title} (${task.priority})`;
        ul.appendChild(li);
    });
}

async function addTask() {
    const title = document.getElementById("task-title").value;
    const priority = document.getElementById("task-priority").value;
    if (!title) return alert("Введите название задачи!");
    await fetch(`${API_URL}/tasks`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ title, priority })
    });
    loadTasks();
}

// ========== ПРИВЫЧКИ ==========
async function loadHabits() {
    const res = await fetch(`${API_URL}/habits`);
    const data = await res.json();
    const ul = document.getElementById("habits");
    if (!ul) return;
    ul.innerHTML = "";
    data.forEach(habit => {
        const li = document.createElement("li");
        li.textContent = habit.name;
        ul.appendChild(li);
    });
}

async function addHabit() {
    const title = document.getElementById("habit-title").value;
    if (!title) return alert("Введите название привычки!");
    await fetch(`${API_URL}/habits`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ name: title })
    });
    loadHabits();
}

// ========== АНАЛИТИКА ==========
async function loadAnalytics() {
    const res = await fetch(`${API_URL}/analytics`);
    const data = await res.json();
    const container = document.getElementById("stats-container");
    if (!container) return;
    container.innerHTML = `
        <p>Всего задач: ${data.total}</p>
        <p>Выполнено: ${data.done} (${data.completion_rate.toFixed(1)}%)</p>
        <p>В работе: ${data.in_progress}</p>
        <p>Запланировано: ${data.todo}</p>
    `;
}

// Автозагрузка данных при открытии страницы
window.onload = () => {
    loadTasks();
    loadHabits();
    loadAnalytics();
};
