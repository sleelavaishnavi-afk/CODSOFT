tasks = []
while True:
    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully.")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
            num = int(input("Enter task number to update: "))
            if num >= 1 and num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num - 1] = new_task
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted successfully.")
            else:
                print("Invalid task number.")
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")