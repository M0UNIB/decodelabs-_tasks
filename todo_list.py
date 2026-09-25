tasks = []


def show_menu():
    print("\n1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Clear all tasks")
    print("5. Exit")


def add_task():
    task = input("Enter a new task: ").strip()
    if task == "":
        print("Task cannot be empty.")
        return
    tasks.append(task)
    print(f"Added: {task}")


def view_tasks():
    if len(tasks) == 0:
        print("There are no tasks yet.")
        return
    print("\nYour to-do list:")
    for number in range(len(tasks)):
        print(f"{number + 1}. {tasks[number]}")


def remove_task():
    if len(tasks) == 0:
        print("There are no tasks to remove.")
        return
    view_tasks()
    choice = input("Enter the number of the task to remove: ")
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        removed = tasks.pop(int(choice) - 1)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number.")


def clear_tasks():
    if len(tasks) == 0:
        print("The list is already empty.")
        return
    tasks.clear()
    print("All tasks cleared.")


def main():
    print("=== To-Do List ===")
    while True:
        show_menu()
        option = input("Choose an option (1-5): ").strip()

        if option == "1":
            add_task()
        elif option == "2":
            view_tasks()
        elif option == "3":
            remove_task()
        elif option == "4":
            clear_tasks()
        elif option == "5":
            print("Goodbye.")
            break
        else:
            print("Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
