# To-Do List Manager (Python CLI App)

## Main Features

- Add tasks with:
  - Name  
  - Category (e.g., School, Work, Health...)  
  - Priority (🔥 Urgent - 🟣 Optional)  
  - Deadline  
  - Frequency (daily, weekly, monthly, none)  
- View tasks sorted by priority and due date  
- Display progress with a pie chart (`matplotlib`)  
- Mark tasks as completed  
- Simulate sending a task via email  
- Smart suggestions for important tasks and category summaries  

---

## Special Logic

- If a task already exists and is added again, its **priority increases automatically** (i.e., the number decreases from 3 to 2).  
- A **progress percentage** is displayed using a pie chart to show completed vs. pending tasks.  
- Tasks are **automatically sorted** by priority and deadline.  
- Suggestions help users focus on **high-priority tasks** with near deadlines.  

---

## Code Structure

The program is divided into the following sections:

1. **Global Configuration**:  
   Contains lists for priority labels, task categories, and frequency options.

2. **Helper Functions**:  
   - Date validation  
   - Category selection  
   - Frequency input  

3. **Core Functionalities**:
   - `add_task()`: Add a new task or raise its priority if it already exists  
   - `view_tasks()`: View tasks and show completion progress  
   - `mark_task_completed()`: Mark a task as done  
   - `simulate_send_email()`: Simulate sending the task info to an email  
   - `suggest_task()`: Suggest tasks based on urgency and show category summary  

4. **Main Menu**:
   - Runs in a loop and lets users choose what to do next.

---

We are beginner programmers working together for the first time.  
Each of us helped write code, test the features, and improve the app step by step.

Thanks for reading about our project! 
