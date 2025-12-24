tasks = []

while True:
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = input("Enter task number to delete: ")

            if num.isdigit():
                num = int(num)
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            else:
                print("Please enter a valid task number.")

    elif choice == "4":
        print("Goodbye 👋")
        break
