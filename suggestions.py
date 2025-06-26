from datetime import datetime
from collections import defaultdict
import random

def suggest_task(task_list): #this funtion help us to create important tasks
    suggestions = []#we keep the tasks
    today = datetime.today().date()
    category_summary = defaultdict(int) #counter per category

    for task in task_list: #We convert the task due date to a date format
        deadline = datetime.strptime(task['deadline'], "%Y-%m-%d").date()
        if not task['completed'] :
            if deadline >= today:
                category_summary[task['category']] += 1
                if task['priority'] <= 2:
                   suggestions.append(task)

    motivational_msgs = [
        "You Got This!",
        "Stay Focused And Keep Going!",
        "You're Doing Great!"
    ]
    print(random.choice(motivational_msgs))
    print("\nSuggested tasks:")
    for task in suggestions:
        print(f"-{task['description']} | Priority {task['priority']} | Due {task['deadline']}")
    print("\nUpcoming tasks by category:")
    for cat, count in category_summary.items():
        print(f"- {count} tasks in '{cat}' are due soon. ")

def show_overdue_tasks(task_list):
    today = datetime.today().date()
    print("\nOverdue tasks:")
    for task in task_list:
        deadline = datetime.strptime(task["deadline"], "%Y-%m-%d").date()
        if not task["completed"] and deadline < today:
            print(f"- {task['description']} ({task['deadline']})")
