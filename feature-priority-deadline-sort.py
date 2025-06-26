from datetime import datetime

# Definiciones globales
PRIORITY_LABELS = {
    1: "🔥 Very High",
    2: "🔴 High",
    3: "🟡 Medium",
    4: "🟢 Low",
    5: "🟣 Very Low"
}

FREQUENCY_OPTIONS = ["none", "daily", "weekly", "monthly"]


# Funciones auxiliares
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_frequency():
    print("Frequency options: none, daily, weekly, monthly")
    freq = input("Enter frequency: ").strip().lower()
    return freq if freq in FREQUENCY_OPTIONS else "none"


# Funciones principales
def add_task(tasks):
    task_name = input("Enter task: ")
    category = input("Enter category (optional): ").strip()

    # Validar prioridad
    while True:
        try:
            priority = int(input("Enter priority (1-5, 1 is highest): "))
            if 1 <= priority <= 5:
                break
            else:
                print("Priority must be between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer.")

    # Validar fecha
    while True:
        deadline_str = input("Enter deadline (YYYY-MM-DD): ")
        if validate_date(deadline_str):
            break
        else:
            print("Invalid date format. Please use YYYY-MM-DD.")

    frequency = get_frequency()

    task = {
        'name': task_name,
        'category': category,
        'priority': priority,
        'label': PRIORITY_LABELS[priority],
        'deadline': deadline_str,
        'frequency': frequency,
        'done': False
    }
    tasks.append(task)
    print(f"Task '{task_name}' added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return

    # Ordenar por prioridad y fecha
    sorted_tasks = sorted(tasks, key=lambda x: (x['priority'], x['deadline']))

    print("\nTo-Do List (Ordered by Priority & Deadline):")
    for i, task in enumerate(sorted_tasks, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{i}. {task['name']} | {task['label']} | Due: {task['deadline']} | Freq: {task['frequency']} [{status}]")


# Menú principal
if __name__ == "__main__":
    tasks = []

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


