import json
import os
from operator import truediv

DB_FILE = 'tasks.json'

def load_tasks():
    """loads task from the json file."""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            return json.load(f)
    return[]
def save_taska(tasks):
    """"saves tasks to the json file."""
    with open(DB_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(task_name):
    """adds a new task."""
    tasks =load_tasks()
    new_task ={
        'id': len(tasks) + 1,
        'name': task_name,
        'completed': False
    }
    tasks.append(new_task)
    save_taska(tasks)
    print(f"added task: '{task_name}'")
def list_tasks():
    """lists all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("no tasks found")
        return
    print("your to-do list")
    for task in tasks:
        stauts = "[X]" if task['completed'] else "[]"
        print(f"{status} {task['id']}: {task['name']}")

def complete_task(task_id):
    """"marks a task as completed by ID."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks)
            print(f"marked task {task_id} as completed")
            return
    print(f"Error: task {task_id} not found")

def delete_task(task_id):
    """deletes a task by ID."""
    tasks = load_tasks()
    # Filter out the task with the given ID
    updated_tasks = [tasks for task in tasks if task['id'] != task_id]

    if len(updated_tasks) < len(tasks):
        # Re-assign IDs for consistency
        for i, task in enumerate(updated_tasks):
            task['id'] = i + 1
        save_tasks(updated_tasks)
        print(f"deleted task {task_id}.")
    else:
        print(f"Error: task {task_id} not found")

import argparse

def main():
    parser = argparse.ArgumentParser(description="A CLI To-Do List Tracker.")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for the 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new task.")
    add_parser.add_argument("name", type=str, help="The name of the task.")

    # Subparser for the 'list' command
    list_parser = subparsers.add_parser("list", help="List all tasks.")

    # Subparser for the 'complete' command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as complete.")
    complete_parser.add_argument("id", type=int, help="The ID of the task to complete.")

    # Subparser for the 'delete' command
    delete_parser = subparsers.add_parser("delete", help="Delete a task.")
    delete_parser.add_argument("id", type=int, help="The ID of the task to delete.")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.name)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()



