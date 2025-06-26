# main.py - Unified To-Do List Application

import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
import random

# ---------- GLOBAL SETTINGS ----------

tasks = []
PRIORITY_LABELS = {
    1: "🔥 Urgent!",
    2: "🔴 Very important",
    3: "🟡 Important",
    4: "🟢 Keep it in mind",
    5: "🟣 Optional"
}
CATEGORIES = ["Home", "School", "Work", "Health", "Personal"]
FREQUENCY_OPTIONS = ["none", "daily", "weekly", "monthly"]

# ---------- HELPER FUNCTIONS ----------

def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def get_frequency():
    print("Frequency options: none, daily, weekly, monthly")
    freq = input("Enter frequency: ").strip().lower()
    return freq if freq in FREQUENCY_OPTIONS else "none"

def choose_category():
    print("Choose a category:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}. {cat}")
    while True:
        try:
            choice = int(input("Category number: "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

# ---------- CORE FUNCTIONALITIES ----------

def add_task():
    name = input("Enter task: ").strip().lower()
    if not name:
        print("Task name cannot be empty.")
        return

    for task in tasks: ## increase the priority of the task
        if task['name'] == name:
            if task['priority'] > 1:
                task['priority'] -= 1
                task['priority_label'] = PRIORITY_LABELS[task['priority']]
                print(f"⚠️ Task already exists. Increased its priority to {task['priority']}.")
            else:
                print("⚠️ Task already exists and is already at the highest priority.")
            return

    category = choose_category()

    while True:
        try:
            priority = int(input("Enter priority (1 = Urgent! - 5 = Optional): "))
            if 1 <= priority <= 5:
                break
            else:
                print("Must be between 1 and 5.")
        except ValueError:
            print("Enter a number.")

    while True:
        deadline_str = input("Enter deadline (YYYY-MM-DD): ")
        deadline = validate_date(deadline_str)
        if deadline:
            break
        else:
            print("Invalid date format.")

    frequency = get_frequency()

    task = {
        'name': name,
        'category': category,
        'priority': priority,
        'priority_label': PRIORITY_LABELS[priority],
        'deadline': deadline_str,
        'frequency': frequency,
        'completed': False
    }
    tasks.append(task)
    print(f"✅ Task '{name}' added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks to show.")
        return

    sorted_tasks = sorted(tasks, key=lambda x: (x['priority'], x['deadline']))
    print("\n📋 Tasks:")
    completed = 0
    for i, t in enumerate(sorted_tasks, 1):
        status = "✔️" if t['completed'] else "❌"
        print(f"{i}. {t['name']} | {t['priority_label']} | Due: {t['deadline']} | {t['category']} | {t['frequency']} [{status}]")
        if t['completed']:
            completed += 1

    total = len(tasks)
    pending = total - completed
    if total > 0:
        print(f"\n📊 Progress: {completed/total*100:.1f}% Completed")
        plt.pie([completed, pending], labels=['Completed', 'Pending'], autopct='%1.1f%%', colors=['#4CAF50', '#FFC107'], startangle=90)
        plt.axis('equal')
        plt.title("Task Completion Progress")
        plt.show()

def mark_task_completed():
    view_tasks()
    try:
        num = int(input("Enter the task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]['completed'] = True
            print(f"✅ Task '{tasks[num-1]['name']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def simulate_send_email():
    view_tasks()
    try:
        num = int(input("Enter task number to email: "))
        if 1 <= num <= len(tasks):
            email = input("Enter recipient's email: ").strip()
            if "@" in email:
                print(f"📨 Simulating sending '{tasks[num-1]['name']}' to {email}... ✅ Email sent!")
            else:
                print("❌ Invalid email format.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

# ---------- SMART SUGGESTIONS ----------

def suggest_task():
    today = datetime.datetime.today().date()
    suggestions = []
    category_summary = defaultdict(int)

    for task in tasks:
        deadline = validate_date(task['deadline'])
        if not task['completed'] and deadline and deadline >= today:
            category_summary[task['category']] += 1
            if task['priority'] <= 2:
                suggestions.append(task)

    print(random.choice([
        "You Got This!", "Stay Focused And Keep Going!", "You're Doing Great!"
    ]))
    print("\nSuggested tasks:")
    for task in suggestions:
        print(f"- {task['name']} | Priority {task['priority']} | Due {task['deadline']}")

    print("\nUpcoming tasks by category:")
    for cat, count in category_summary.items():
        print(f"- {count} tasks in '{cat}' are due soon.")

# ---------- MAIN MENU ----------

if __name__ == "__main__":
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks & Progress")
        print("3. Mark Task as Completed")
        print("4. Suggest Tasks")
        print("5. Send Task by Email")
        print("6. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            add_task()
        elif option == "2":
            view_tasks()
        elif option == "3":
            mark_task_completed()
        elif option == "4":
            suggest_task()
        elif option == "5":
            simulate_send_email()
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
