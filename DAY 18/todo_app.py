import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    """Loads tasks from the JSON file. Returns an empty list if file doesn't exist."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: JSON file is corrupted. Starting with an empty list.")
            return []
    return []

def save_tasks(tasks):
    """Saves the tasks list to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    print("\n--- Add Task ---")
    description = input("Enter task description: ").strip()
    
    if not description:
        print("Task description cannot be empty!")
        return

    for t in tasks:
        if t["task"].lower() == description.lower():
            print("This task already exists!")
            return

    new_task = {
        "task": description,
        "completed": False
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("No tasks found! Enjoy your free time.")
        return

    for index, item in enumerate(tasks, start=1):
        status = "[X]" if item["completed"] else "[ ]"
        print(f"{index}. {status} {item['task']}")

def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to mark complete: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to delete: "))
        if 1 <= choice <= len(tasks):
            deleted = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Task '{deleted['task']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n" + "="*30)
        print("        TO-DO LIST APP        ")
        print("="*30)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        print("="*30)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting application. Have a productive day!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()