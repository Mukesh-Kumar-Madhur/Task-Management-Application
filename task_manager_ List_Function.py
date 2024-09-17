import os
from datetime import datetime, timedelta
from tabulate import tabulate
from collections import defaultdict

# Constants for file names
USER_FILE = 'user.txt'
TASK_FILE = 'tasks.txt'

def ensure_file_exists(file_name):
    """Ensure that a file exists, otherwise create it to avoid file not found error."""
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            pass

def read_users():
    """
    Read users from the USER_FILE and return them as a dictionary.
    
    The function reads each line from the USER_FILE, where each line contains a 
    username and password separated by a comma. It then stores these as key-value 
    pairs in a dictionary and returns this dictionary.
    
    Returns:
        dict: A dictionary where the keys are usernames and the values are passwords.
    """
    
    users = {}  # Initialize an empty dictionary to store user data
    
    # Ensure that the USER_FILE exists before trying to read from it
    ensure_file_exists(USER_FILE)
    
    # Open the USER_FILE in read mode
    with open(USER_FILE, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip any leading/trailing whitespace and split the line into username and password
            username, password = line.strip().split(', ')
            
            # Store the username and password in the dictionary
            users[username] = password
    
    # Return the dictionary containing all the users and their passwords
    return users


def read_tasks():  # reading Task file
    """Ensure TASK_FILE exists."""
    ensure_file_exists(TASK_FILE)

def login(users):
    """
    Log in the user by verifying their credentials.

    This function prompts the user for their username and password and verifies these 
    credentials against the provided dictionary of users. If the credentials are correct, 
    the function prints a success message and returns the username. If the credentials 
    are incorrect, it provides feedback and prompts the user to try again.

    Returns:
        str: The username if login is successful.
    """
    
    while True:  # Start an infinite loop to repeatedly prompt the user until they log in successfully
        # Prompt the user to enter their username
        username = input("Enter your username: ")
        
        # Check if the entered username exists in the users dictionary
        if username in users:
            # Prompt the user to enter their password
            password = input("Enter your password: ")
            
            # Verify if the entered password matches the stored password for the username
            if password == users[username]:
                # Print a success message and return the username if credentials are correct
                print(f"Login successful! Welcome, {username}.")
                return username
            else:
                # Print an error message if the password is incorrect and prompt again
                print("Invalid password. Please try again.")
        else:
            # Print an error message if the username is not found and prompt again
            print("Username not found. Please try again.")


def register_user(users):
    """
    Register a new user, ensuring no duplicate usernames.

    This function prompts the user to enter a new username and password. It checks if 
    the username already exists in the `users` dictionary. If the username is unique, 
    it then prompts the user to confirm the password. If the passwords match, it adds 
    the new user's credentials to both the `users` dictionary and the USER_FILE.

    Args:
        users (dict): A dictionary where keys are usernames and values are passwords.

    Returns:
        None
    """
    
    while True:  # Start an infinite loop to repeatedly prompt until a successful registration
        # Prompt the user to enter a new username
        new_username = input("Enter new username: ")
        
        # Check if the entered username already exists in the users dictionary
        if new_username in users:
            # Print an error message if the username already exists and prompt again
            print("Username already exists. Please choose another one.")
        else:
            # Prompt the user to enter a new password
            new_password = input("Enter new password: ")
            # Prompt the user to confirm the new password
            confirm_password = input("Confirm password: ")
            
            # Check if the entered passwords match
            if new_password == confirm_password:
                # Open the USER_FILE in append mode to add the new user
                with open(USER_FILE, 'a') as file:
                    # Write the new username and password to the file
                    file.write(f"{new_username}, {new_password}\n")
                
                # Add the new user's credentials to the users dictionary
                users[new_username] = new_password
                
                # Print a success message and exit the function
                print("Registration successful!")
                return
            else:
                # Print an error message if the passwords do not match and prompt again
                print("Passwords do not match. Please try again.")


def add_task():
    """
    Add a new task to TASK_FILE.

    This function prompts the user to enter details for a new task, including the username 
    of the person the task is assigned to, the title, description, and due date. It validates 
    the username and the date format before saving the task details to TASK_FILE.

    Returns:
        None
    """
    
    # Read existing users from USER_FILE to validate the assigned username
    users = read_users()
    
    # Loop to ensure a valid username is entered
    while True:
        username = input("Enter username of the person the task is assigned to: ")
        if username in users:
            break  # Exit loop if the username is found
        else:
            print("Username not found. Please enter a valid username.")
    
    # Prompt for task details
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    
    # Loop to ensure the due date is in the correct format
    while True:
        due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
        try:
            # Validate the date format
            datetime.strptime(due_date, "%Y-%m-%d")
            break  # Exit loop if date format is correct
        except ValueError:
            # Print an error message if the date format is incorrect
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    # Get the current date for the assigned date
    assigned_date = datetime.today().strftime("%Y-%m-%d")
    # Set the initial completion status to 'No'
    completion_status = 'No'
    
    # Append the new task details to TASK_FILE
    with open(TASK_FILE, 'a') as file:
        file.write(f"{username}, {title}, {description}, {assigned_date}, {due_date}, {completion_status}\n")
    
    # Print a success message after the task is added
    print("Task added successfully!")


def view_all_tasks():
    """
    Display all tasks in TASK_FILE.

    This function reads tasks from TASK_FILE and displays them in a tabular format. 
    It ensures that the file exists, reads the tasks from the file, and formats 
    them for a user-friendly display.

    Returns:
        None
    """
    
    # Ensure that the TASK_FILE exists; if it doesn't, create an empty file
    ensure_file_exists(TASK_FILE)
    
    # Initialize an empty list to store all tasks read from the file
    tasks = []
    
    # Open TASK_FILE in read mode
    with open(TASK_FILE, 'r') as file:
        # Read each line from the file
        for line in file:
            # Remove leading/trailing whitespace and split the line into task details
            task_details = line.strip().split(', ')
            # Append the task details to the tasks list
            tasks.append(task_details)
    
    # Define headers for the table to describe each column of the task details
    headers = ["Assigned To", "Title", "Description", "Assigned Date", "Due Date", "Completed"]
    
    # Print a header for the output
    print("\nAll Tasks:")
    # Use tabulate to display the tasks in a formatted table with headers
    print(tabulate(tasks, headers=headers, tablefmt="pretty"))




def view_my_tasks(username):
    """
    Display tasks assigned to the logged-in user and allow them to mark tasks as complete 
    or edit task details (like the assigned username or due date).
    
    Parameters:
    username (str): The username of the logged-in user.
    """
    # Ensure the task file exists before trying to read from it
    ensure_file_exists(TASK_FILE)
    
    all_tasks = []   # List to store all tasks from the file
    user_tasks = []  # List to store only the tasks assigned to the logged-in user
    
    try:
        # Open the task file in read mode
        with open(TASK_FILE, 'r') as file:
            for line in file:
                # Split each line into task details and remove any extra spaces
                task_details = line.strip().split(', ')
                
                # Add the task to the list of all tasks
                all_tasks.append(task_details)
                
                # If the task is assigned to the logged-in user, add it to user_tasks
                if task_details[0] == username:
                    user_tasks.append(task_details)
    except FileNotFoundError:
        # This block runs if the task file is not found
        print("Tasks file not found. Please ensure that tasks are available.")
        return  # Exit the function
    except Exception as e:
        # This block handles any other errors that occur during file reading
        print(f"An error occurred while reading the tasks: {e}")
        return  # Exit the function
    
    # Check if there are any tasks assigned to the logged-in user
    if user_tasks:
        # Define table headers for displaying tasks
        headers = ["No.", "Assigned To", "Title", "Description", "Assigned Date", "Due Date", "Completed"]
        
        # Create a numbered list of tasks for the user
        numbered_tasks = [[i + 1] + task for i, task in enumerate(user_tasks)]
        
        # Display the tasks in a table format using the tabulate module
        print(f"\nTasks assigned to {username}:")
        print(tabulate(numbered_tasks, headers=headers, tablefmt="pretty"))
        
        while True:
            try:
                # Prompt the user to select a task by number, or return to the main menu
                task_no = int(input("Enter the task number to select a task, or -1 to return to the main menu: "))
                
                if task_no == -1:
                    # If the user enters -1, exit the loop and return to the main menu
                    return
                elif 1 <= task_no <= len(user_tasks):
                    # If the user enters a valid task number, proceed to task actions
                    selected_task = user_tasks[task_no - 1]
                    
                    # Display options to either mark the task as complete or edit it
                    print("\n1 - Mark as complete")
                    print("2 - Edit task")
                    action = int(input("Enter the action number: "))
                    
                    if action == 1:
                        # Mark the selected task as complete by setting the "Completed" field to 'Yes'
                        selected_task[5] = 'Yes'
                        
                        # Update the task file with the modified task list
                        update_task_in_file(all_tasks)
                        print("Task marked as complete.")
                    
                    elif action == 2:
                        # Prompt the user for a new username and due date
                        new_username = input(f"Enter new username (current: {selected_task[0]}): ")
                        new_due_date = input(f"Enter new due date (YYYY-MM-DD) (current: {selected_task[4]}): ")
                        
                        # Validate the date format and ensure the due date is not in the past
                        try:
                            new_due_date_obj = datetime.strptime(new_due_date, "%Y-%m-%d")
                            if new_due_date_obj < datetime.now():
                                print("Due date cannot be in the past. Task not updated.")
                                continue  # Skip the rest of the loop and prompt the user again
                            
                            # Find and update the selected task in the all_tasks list
                            for task in all_tasks:
                                if task == selected_task:
                                    task[0] = new_username  # Update the username
                                    task[4] = new_due_date  # Update the due date
                                    break
                            
                            # Write the updated task list back to the file
                            update_task_in_file(all_tasks)
                            print("Task updated successfully.")
                        except ValueError:
                            # Handle invalid date format input
                            print("Invalid date format. Task not updated.")
                    
                    else:
                        # Handle invalid action number input
                        print("Invalid action number.")
                else:
                    # Handle invalid task number input
                    print("Invalid task number.")
            except ValueError:
                # Handle invalid input that cannot be converted to an integer
                print("Please enter a valid number.")
    else:
        # If there are no tasks assigned to the user, inform them
        print("No tasks assigned to you.")

def update_task_in_file(tasks):
    """
    Write the updated list of tasks back to the task file.
    
    Parameters:
    tasks (list): A list of tasks where each task is a list of its details.
    """
    try:
        # Open the task file in write mode to overwrite the existing content
        with open(TASK_FILE, 'w') as file:
            for task in tasks:
                # Write each task as a comma-separated string followed by a newline
                file.write(', '.join(task) + '\n')
    except Exception as e:
        # Handle any errors that occur during file writing
        print(f"An error occurred while updating the tasks: {e}")





def display_statistics():
    """
    Read and display statistics from the 'task_overview.txt' and 'user_overview.txt' report files.
    The statistics are displayed in a clear tabular format for easy readability.
    """

    # Ensure that both report files exist before proceeding
    ensure_file_exists('task_overview.txt')
    ensure_file_exists('user_overview.txt')

    # Display the content of 'task_overview.txt'
    print("\nTask Overview:")
    with open('task_overview.txt', 'r') as file:
        print(file.read())  # Simply read and print the entire file content

    # Initialize a list to store user statistics and a dictionary for the current user's stats
    print("\nUser Overview:")
    user_stats = []  # List to store statistics for each user
    current_user_stats = {}  # Dictionary to store stats for the currently processed user
    
    # Read and process the content of 'user_overview.txt'
    with open('user_overview.txt', 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace from the line
            if line.startswith("User:"):
                # If we've started a new user section, save the previous user's stats (if any)
                if current_user_stats:
                    user_stats.append(current_user_stats)
                
                # Start a new user stats dictionary for the current user
                current_user_stats = {"User": line.split(": ")[1]}  # Extract the username
            elif line:
                # Process other lines that contain key-value pairs
                try:
                    key, value = line.split(": ")
                    current_user_stats[key] = value  # Store the key-value pair in the current user's stats
                except ValueError:
                    # Handle any lines that do not follow the expected "key: value" format
                    print(f"Line not in expected format: {line}")  # Debug print for unexpected format
        if current_user_stats:
            # Add the last user's stats to the list
            user_stats.append(current_user_stats)
    
    # Prepare table headers and data for displaying user statistics
    headers = ["User", "Total tasks", "Task percentage", "Completed tasks", "Incomplete tasks", "Overdue tasks"]
    table_data = [[
        stat.get("User", ""), 
        stat.get("Total tasks", ""), 
        stat.get("Task percentage", ""), 
        stat.get("Completed tasks", ""), 
        stat.get("Incomplete tasks", ""), 
        stat.get("Overdue tasks", "")
    ] for stat in user_stats]
    
    # Display the user statistics in a table format
    print(tabulate(table_data, headers=headers, tablefmt="pretty"))



def generate_reports():
    """
    Generate reports summarizing the tasks and users' task-related statistics.
    The reports are saved to 'task_overview.txt' and 'user_overview.txt'.
    """

    # Initialize counters for task statistics
    total_tasks = 0
    completed_tasks = 0
    incomplete_tasks = 0
    overdue_tasks = 0
    
    # Dictionary to track task statistics per user
    user_task_counts = defaultdict(lambda: {'total': 0, 'completed': 0, 'incomplete': 0, 'overdue': 0})
    
    # Get the current date to compare with task due dates
    today = datetime.today()

    # Read the task file and process each task
    with open(TASK_FILE, 'r') as file:
        for line in file:
            total_tasks += 1  # Increment the total task count
            task_details = line.strip().split(', ')
            username, _, _, _, due_date_str, completion_status = task_details
            
            # Convert the due date string to a datetime object for comparison
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
            
            # Update the user's total task count
            user_task_counts[username]['total'] += 1
            
            if completion_status == 'Yes':
                # If the task is completed, increment the completed tasks count
                completed_tasks += 1
                user_task_counts[username]['completed'] += 1
            else:
                # If the task is incomplete, increment the incomplete tasks count
                incomplete_tasks += 1
                user_task_counts[username]['incomplete'] += 1
                
                if due_date < today:
                    # If the task is overdue, increment the overdue tasks count
                    overdue_tasks += 1
                    user_task_counts[username]['overdue'] += 1

    # Calculate statistics and prepare the content for 'task_overview.txt'
    total_users = len(user_task_counts)
    task_overview_content = (
        f"Total tasks: {total_tasks}\n"
        f"Completed tasks: {completed_tasks}\n"
        f"Incomplete tasks: {incomplete_tasks}\n"
        f"Overdue tasks: {overdue_tasks}\n"
        f"Incomplete tasks percentage: {incomplete_tasks / total_tasks * 100:.2f}%\n"
        f"Overdue tasks percentage: {overdue_tasks / total_tasks * 100:.2f}%\n"
    )
    
    # Write the task overview to 'task_overview.txt'
    with open('task_overview.txt', 'w') as file:
        file.write(task_overview_content)
    
    # Prepare the content for 'user_overview.txt'
    user_overview_content = (
        f"Total users: {total_users}\n"
        f"Total tasks: {total_tasks}\n\n"
    )
    
    # Add statistics for each user to the user overview content
    for user, counts in user_task_counts.items():
        task_percentage = counts['total'] / total_tasks * 100
        user_overview_content += (
            f"User: {user}\n"
            f"Total tasks: {counts['total']}\n"
            f"Task percentage: {task_percentage:.2f}%\n"
            f"Completed tasks: {counts['completed']}\n"
            f"Incomplete tasks: {counts['incomplete']}\n"
            f"Overdue tasks: {counts['overdue']}\n\n"
        )
    
    # Write the user overview to 'user_overview.txt'
    with open('user_overview.txt', 'w') as file:
        file.write(user_overview_content)


def main():
    read_tasks()
    users = read_users()
    current_user = login(users)
    
    while True:
        print("\nMenu:")
        print("a - Add task")
        print("va - View all tasks")
        print("vm - View my tasks")
        if current_user == 'admin':
            print("r - Register new user")
            print("ds - Display statistics")
            print("gr - Generate reports")
        print("e - Exit")
        
        option = input("Enter your choice: ").lower()
        if option == 'a':
            add_task()
        elif option == 'va':
            view_all_tasks()
        elif option == 'vm':
            view_my_tasks(current_user)
        elif option == 'r' and current_user == 'admin':
            register_user(users)
        elif option == 'ds' and current_user == 'admin':
            display_statistics()
        elif option == 'gr' and current_user == 'admin':
            generate_reports()
            print("Reports generated successfully.")
        elif option == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
