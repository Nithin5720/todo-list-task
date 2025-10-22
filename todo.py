# todo.py

# --- Function to load tasks from file ---
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# --- Function to save tasks to file ---
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# --- Main Program ---
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            if len(tasks) == 0:
                print("\nNo tasks found!")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == '2':
            new_task = input("\nEnter a new task: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)
                print(f"✅ Task '{new_task}' added successfully!")
            else:
                print("⚠️ Task cannot be empty.")

        elif choice == '3':
            if len(tasks) == 0:
                print("\nNo tasks to remove.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Enter task number to remove: "))
                    if 1 <= task_num <= len(tasks):
                        removed = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"🗑️ Task '{removed}' removed.")
                    else:
                        print("⚠️ Invalid task number.")
                except ValueError:
                    print("⚠️ Please enter a valid number.")

        elif choice == '4':
            print("\nGoodbye! 👋 Your tasks are saved.")
            break

        else:
            print("⚠️ Invalid choice. Please enter 1–4.")

if __name__ == "__main__":
    main()
