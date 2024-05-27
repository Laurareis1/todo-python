import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def get_tasks():
    return tasks

def add_task(description):
    task_id = len(tasks) + 1
    tasks.append({'id': task_id, 'description': description, 'completed': False})
    save_tasks()
    print(f"Tarefa '{description}' adicionada com sucesso!")

def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks()
            print(f"Tarefa '{task['description']}' marcada como concluída.")
            return
    print("Tarefa não encontrada.")

load_tasks()
