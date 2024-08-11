# Global list to store tasks developed by a junior pythonist called George Stanley and he is still learning more so expect more upcoming
import cowsay
from random import randint
tasks = []

def main():
    random_detail()
    menu_ribbon()

def menu_ribbon():
    while True: 
        print("\n:::::---------TO-DO-LIST APPLICATION-------::::::")
        print("1. Add a new Task.")
        print("2. Remove Task from list.")
        print("3. Show available list.")
        print("4. Mark Task as Priority.")
        print("5. Edit an existing item.") 
        print("6. Exit the application. ")    

        try:
            option = int(input("Choose your option (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if option == 1:
            new_task = input("New Task: ")
            add_task(new_task)
        elif option == 2:
            remove_task()
        elif option == 3:
            show_tasks()
        elif option == 4:
            mark_priority()
        elif option == 5:
            edit_task()
        elif option == 6:
            ending_program()
        else:
            print("Invalid option. Kindly choose a number that is synta'.")

def add_task(task):
    tasks.append({"task": task, "priority": False})
    cowsay.daemon(f"'{task}' has been successfully added as a new task.")
    
def remove_task():
    show_tasks()
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task['task']}' has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    
def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nHere is your list of tasks:")
        for i, task in enumerate(tasks, 1):
            priority = "Priority" if task["priority"] else "Normal"
            print(f"{i}. {task['task']} ({priority})")

def mark_priority():
    show_tasks()
    try:
        index = int(input("Enter the number of the task to mark as priority: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["priority"] = True
            print(f"Task '{tasks[index]['task']}' marked as priority.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def edit_task():
    show_tasks()
    try:
        index = int(input("Enter the number of the task to edit: ")) - 1
        if 0 <= index < len(tasks):
            new_description = input("Enter the new description: ")
            tasks[index]["task"] = new_description
            print(f"Task has been updated to '{new_description}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
def ending_program():
    print(f"\n Great work going through the project i built, have a great time ahead !!! \n ")
    exit()
def random_detail():
    lucky_number = randint(1,4)
    if lucky_number == 1:
        print("You will be better someday okay")
    elif lucky_number == 2:
        print("You know no one is better than who you are right")
    elif lucky_number == 3:
        print("Someone will always be watching everything you do so be careful okay")
    else:
        print("You know you are never too late to keep on dreaming and making it happen")

main()
