import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
"""
# Global task list
tasks = []

# Predefined categories
available_categories = ["Home", "School", "Work", "Health", "Personal"]


def choose_category():
    print("Choose a category:")
    for idx, cat in enumerate(available_categories, 1):
        print(f"{idx}. {cat}")

    while True:
        try:
            choice = int(input("Category number: "))
            if 1 <= choice <= len(available_categories):
                return available_categories[choice - 1]
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")


def add_task_interactive():
    description = input("Enter task description: ").strip().lower()
    if not description:
        print("Task description cannot be empty.")
        return

    for task in tasks: ## check task repeated
        if task['description'] == description:
            if task['priority'] > 1:
                task['priority'] -= 1  # Increase priority
                print(f"⚠️ Task already exists. Increased its priority to {task['priority']}.\n")
            else:
                print("⚠️ Task already exists and is already at the highest priority.\n")
            return # Skip adding duplicate

    while True:  ## priority input
        try:
            priority = int(input("Enter priority (1=Very High to 5=Low): "))
            if 1 <= priority <= 5:
                break
            else:
                print("Priority must be between 1 and 5.")
        except ValueError:
            print("Enter a valid number between 1 and 5.")

    while True: ## deadline input
        deadline_str = input("Enter deadline (YYYY-MM-DD): ")
        try:
            deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    category = choose_category()

    task = {
        'description': description,
        'priority': priority,
        'deadline': str(deadline),
        'category': category,
        'completed': False
    }
    tasks.append(task)
    print(f"\n✅ Task added: {description} - Priority {priority}, Deadline {deadline}, Category {category}\n")


def view_tasks_and_show_progress():
    if not tasks:
        print("📭 No tasks to show.\n")
        return

    print("\n📋 Current Tasks:")
    completed_count = 0
    for i, t in enumerate(tasks, 1):
        status = "✔️ Done" if t['completed'] else "❌ Pending"
        print(
            f"{i}. {t['description']} - Priority {t['priority']} - Due: {t['deadline']} - Category: {t['category']} - {status}")
        if t['completed']:
            completed_count += 1

    total = len(tasks)
    pending_count = total - completed_count
    completed_percent = (completed_count / total) * 100

    print(f"\n📊 Progress: {completed_percent:.1f}% Completed\n")

    # Pie chart
    labels = ['Completed', 'Pending']
    sizes = [completed_count, pending_count]
    colors = ['#4CAF50', '#FFC107']
    explode = (0.1, 0)

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90, explode=explode)
    plt.axis('equal')
    plt.title("Task Completion Progress")
    plt.show()

def mark_task_completed():
    if not tasks:
        print("📭 No tasks available.\n")
        return

    print("\n📝 Choose a task to mark as completed:")
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t['completed'] else "❌"
        print(f"{i}. {t['description']} - Priority {t['priority']} - {status}")

    while True:
        try:
            selection = int(input("Enter the task number: "))
            if 1 <= selection <= len(tasks):
                if tasks[selection - 1]['completed']:
                    print("🔁 That task is already marked as completed.")
                else:
                    tasks[selection - 1]['completed'] = True
                    print(f"✅ Task '{tasks[selection - 1]['description']}' marked as completed.")
                break
            else:
                print("Out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a task number.")

def simulate_send_email():
    if not tasks:
        print("📭 No tasks to send.\n")
        return

    print("\n📧 Choose a task to send by email:")
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t['completed'] else "❌"
        print(f"{i}. {t['description']} - Priority {t['priority']} - Due: {t['deadline']} - {status}")

    while True:
        try:
            selection = int(input("Enter the task number to send: "))
            if 1 <= selection <= len(tasks):
                break
            else:
                print("Invalid number. Try again.")
        except ValueError:
            print("Please enter a valid number.")

    email = input("Enter the recipient's email: ").strip()
    if not email or "@" not in email:
        print("⚠️ Invalid email format. Cancelled.")
        return

    task = tasks[selection - 1]
    print(f"\n📨 Simulating sending task: '{task['description']}' to {email}...")
    print(f"✅ Email sent to {email}!\n")


### Test
if __name__ == "__main__":
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks & Progress")
        print("3. Mark Task as Completed")
        print("4. Send Task by Email")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task_interactive()
        elif choice == "2":
            view_tasks_and_show_progress()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            simulate_send_email()
        elif choice == "5":
            print("👋 Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
"""

# main.py - Unified To-Do List Application

import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
import random

# ---------- GLOBAL SETTINGS ----------

tasks = []
PRIORITY_LABELS = {
    1: "🔥 Very High",
    2: "🔴 High",
    3: "🟡 Medium",
    4: "🟢 Low",
    5: "🟣 Very Low"
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
            priority = int(input("Enter priority (1 = Very high - 5 = Very low): "))
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
