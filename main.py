import json 

TASKS_FILE = "task.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Task title: ")
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{index}. [{status}] {task['title']}")


def complete_task(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input("Task number to complete: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return

    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks)
        print("Task completed!")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    list_tasks(tasks)

    if not tasks:
        return

    try:
        index = int(input("Task number to delete: ")) - 1
    except ValueError:
        print("Please enter a valid number.")
        return

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()