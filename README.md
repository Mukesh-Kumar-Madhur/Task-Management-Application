```markdown
# Task Management Application

## Description
The **Task Management Application** is a command-line tool that allows users to manage tasks in a simple and effective way. It supports user login, task creation, viewing, and task updates such as marking them as completed or editing details like due dates and assigned users. The application uses text files (`user.txt` and `tasks.txt`) to store user credentials and task data.

## Features
- **User Login & Registration**: Users can register new accounts, and log in with their credentials.
- **Task Management**: Tasks can be assigned to users, viewed in tabular format, edited, and marked as complete.
- **Input Validation**: The application ensures that usernames, passwords, and due dates are valid before processing.
- **File Handling**: The application ensures that required files are created and handled appropriately.

## Requirements
- Python 3.x
- `tabulate` module (for displaying tasks in table format)

To install the required `tabulate` module, run:
```bash
pip install tabulate
```

## Files
- `user.txt`: Stores the registered usernames and passwords.
- `tasks.txt`: Stores the task details such as assigned user, task title, description, assigned date, due date, and completion status.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-management-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd task-management-app
   ```
3. Run the script:
   ```bash
   python task_manager.py
   ```

## Usage
Upon running the script, the following options are presented:
1. **Login**: Users can log in with their credentials.
2. **Register**: New users can register a unique username and password.
3. **Add Task**: Adds a new task, specifying the assigned user, task details, and due date.
4. **View All Tasks**: Displays all tasks in a tabular format.
5. **View My Tasks**: Displays tasks assigned to the logged-in user, with options to mark them as complete or edit the task.

## Example
```plaintext
Enter your username: admin
Enter your password: adm1n
Login successful! Welcome, admin.

Options:
1 - Add Task
2 - View All Tasks
3 - View My Tasks
4 - Exit

Select an option: 2

All Tasks:
+------------+-------------+--------------------+-----------------+------------+------------+-----------+
| Assigned To |    Title    |     Description    |  Assigned Date  |  Due Date  | Completed |
+------------+-------------+--------------------+-----------------+------------+------------+-----------+
|    user1   |  Task Title  |  Task Description  |   2023-09-15    |  2023-09-20|    No     |
+------------+-------------+--------------------+-----------------+------------+------------+-----------+
```

## License
This project is licensed under the MIT License.
```
