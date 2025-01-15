# To-Do List Application

## Description
The To-Do List Application is a simple command-line tool to help users manage their daily tasks. Users can add tasks, view their list of tasks, delete tasks, and exit the program. It is built using Python and demonstrates basic programming concepts such as loops, error handling, and user input validation.

---

## Features:
  - Add Tasks: Allows users to add tasks to their to-do list.
  - View Tasks: Displays the tasks in a neatly numbered format.
  - Delete Tasks: Removes a task from the list based on the task number.
  - Quit: Exits the application gracefully.

---

## How to Use
### 1. Prerequisites
  Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Running the Application
1. Save the application code in a file named `to_do_list.py`.
2. Open a terminal or command prompt.
3. Navigate to the folder where the file is saved using the `cd` command.
4. Run the script with the following command:
   ```
   python to_do_list.py
   ```

### 3. Using the Menu
When the program starts, you will see the main menu:
```
Welcome to To-Do List Application!
1. Add Task
2. View Tasks
3. Delete Task
4. Quit
```
  Enter the number corresponding to your desired action.
  Follow the on-screen prompts to add, view, or delete tasks.
  To exit, select option `4`.

---

## Error Handling
  - Invalid Input: If you enter an invalid menu option or task number, the program will alert you and prompt you to try again.
  - Empty Task List: The program will notify you if you try to view or delete tasks when the list is empty.
  - Task Deletion: If you attempt to delete a task using an invalid number, the program will notify you.
  - The program uses `try`, `except`, and `finally` blocks to handle errors and ensure smooth execution.

---

## Code Organization
The application is organized into functions for clarity and maintainability:
- `display_menu()`: Displays the main menu.
- `add_task(tasks)`: Adds a task to the list.
- `view_tasks(tasks)`: Displays all tasks in the list.
- `delete_task(tasks)`: Deletes a task based on user input.
- `main()`: Orchestrates the program’s flow and handles user interaction.

---


## Future Enhancements
- Save tasks to a file for persistence.
- Allow task editing.
- Add task priorities or deadlines.
- Develop a graphical user interface (GUI).

---

## License
This project is open-source and available for educational and personal use. Feel free to modify and enhance it as needed.

