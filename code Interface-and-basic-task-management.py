#Interface-and-basic-task-management
PRIORITY_LABELS = {
    1: "🔥 Very High",
    2: "🔴 High",
    3: "🟡 Medium",
    4: "🟢 Low",
    5: "🟣 Very Low"
}

def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
    
FREQUENCY_OPTIONS = ["none", "daily", "weekly", "monthly"]

def get_frequency():
    print("Frequency options: none, daily, weekly, monthly")
    freq = input("Enter frequency: ").strip().lower()
    return freq if freq in FREQUENCY_OPTIONS else "none"

def add_task(tasks):
    task_name = input("Enter task: ")

    # Categoría (si otro miembro la implementa)
    category = input("Enter category (optional): ").strip()

    # Prioridad
    while True:
        try:
            priority = int(input("Enter priority (1-5, 1 is highest): "))
            if 1 <= priority <= 5:
                break
            else:
                print("Priority must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer.")

    # Fecha de entrega
    while True:
        deadline_str = input("Enter deadline (YYYY-MM-DD): ")
        deadline = validate_date(deadline_str)
        if deadline:
            break
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Frecuencia
    frequency = get_frequency()

    task = {
        'task': task_name,
        'category': category,
        'priority': priority,
        'priority_label': PRIORITY_LABELS[priority],
        'deadline': deadline_str,
        'frequency': frequency,
        'done': False
    }
    tasks.append(task)

def show_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return

    sorted_tasks = sorted(tasks, key=lambda x: (x['priority'], x['deadline']))
    for i, task in enumerate(sorted_tasks, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['task']} | {task['priority_label']} | Due: {task['deadline']} | Freq: {task['frequency']} [{status}]")
