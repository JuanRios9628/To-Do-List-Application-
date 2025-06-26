# 📝 To-Do List Manager (Python CLI App)

 Main Features
- Add tasks with:
  - Name
  - Category (e.g., School, Work, Health...)
  - Priority (🔥 Very High - 🟣 Very Low)
  - Deadline
  - Frequency (daily, weekly, monthly, none)
-  View tasks sorted by priority and due date
-  Display progress with a pie chart (matplotlib)
-  Mark tasks as completed
-  Simulate sending a task via email
-  Smart suggestions for important tasks and category summaries

🧠 Special Logic

- If a task already exists and is added again, its **priority increases automatically** (i.e., the number decreases from 3 to 2).
- A **progress percentage bar** is shown with a pie chart to visualize overall task status.
- Tasks are **automatically sorted** by priority and deadline.
- Suggestions help users focus on high-priority tasks with approaching deadlines.

📂 Code Structure

The program is divided into the following sections:

1. **Global Configuration**: lists, priority labels, and categories.
2. **Helper Functions**: date validation, category selection, frequency input.
3. **Core Functionalities**:
   - `add_task()`: Add a new task or raise priority if it already exists.
   - `view_tasks()`: View all tasks and progress.
   - `mark_task_completed()`: Mark a task as completed.
   - `simulate_send_email()`: Simulate sending task via email.
   - `suggest_task()`: Show recommendations and category summary.
4. **Interactive Menu** using a `while` loop.

🛠️ Requirements
- Python 3.x
- `matplotlib` library (for charts)
You can install matplotlib using:
```bash
pip install matplotlib
🚀 How to Run
Clone the repository:

bash
Copiar
Editar
git clone https://github.com/your_username/to-do-list-python.git
cd to-do-list-python
Run the main script:

bash
Copiar
Editar
python your_filename.py
