# ============== SIMPLE TO-DO LIST MANAGER ==============

# Store tasks as a list of dictionaries: {'task': 'Buy milk', 'completed': False}
tasks = []

def add_task():
    task_name = input("Enter the task: ").strip()
    if task_name:
        tasks.append({'task': task_name, 'completed': False})
        print(f"Task '{task_name}' added successfully!")
    else:
        print("Task cannot be empty!")

def view_tasks():
    if not tasks:
        print("No tasks yet! Add some tasks first.")
        return
    
    print("\n============= YOUR TO-DO LIST =============")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task['completed'] else " "
        print(f"{i}. [{status}] {task['task']}")
    print("==========================================\n")

def mark_completed():
    view_tasks()
    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]['completed'] = True
            print(f"Task {num} marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Task '{removed['task']}' deleted!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main program loop
while True:
    print("\n============= TO-DO LIST MENU =============")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print("==========================================")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Goodbye! Stay productive! 👋")
        break
    else:
        print("Invalid choice! Please enter 1-5.")