# To Do List Application

# Project requirements:
# Build simple command line interface(ClI) welcomes users and displays menu.
# The task should be stored in a python list.

# Core Features:
# Add tasks
# View tasks
# Delete tasks
# Quit the application

# User interaction
# Use input() to capture user selections and ensure proper input validation to hand invalid choices.

# Error handling:
# Implement error handling using try, except, else and finally blocks
# Alert the user if they provide invalid input
# Alert the user if there are no tasks to view.
# Alert the user if they try to delete a task that doesn't exist
# Alert the user if they select an option on the main menu that doesn't exist

# Code Organization
# Organize your code into functions to improve clarity and maintainability
# Use descriptive function names and add comments/docstrings where necessary

# Testing and Debugging
# Thoroughly test your application, considering edge cases such as empty lits and invalid input.

def display_menu():
    """Display main menu options"""
    print("\nWelcome to To-Do list Application!")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("Invalid input, try again!")


def view_task(tasks):
    """View all tasks in the list."""
    if tasks:
        print("\nYour Tasks")
        # enumerate gives both the index and the task from the list.
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}, {task}")
    else:
        print("There are no Tasks!")


def delete_task(tasks):
    """Delete a task by its number"""
    if tasks:
        try:
            view_task(tasks)
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted.")
            else:
                print("Invalid task number. Try again!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        finally:
            print("Returning to the main menu...")
    else:
        print("There are no tasks!")


def main():
    """Main function to run the application."""
    tasks = []
    while True:
        display_menu()
        try:
            user_choice = int(
                input("Which task would like to perform?(1-4): "))
            if user_choice == 1:
                add_task(tasks)
            elif user_choice == 2:
                view_task(tasks)
            elif user_choice == 3:
                delete_task(tasks)
            elif user_choice == 4:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")


main()
