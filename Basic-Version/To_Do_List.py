import os

# --------------------------------[ Helper Functions ]-----------------------------------

def clear_screen():
    """
    Clears the console screen based on the operating system.
    """
    # Check OS: 'nt' Is For Windows, 'clear' Is For Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------------[ Core Features ]-----------------------------------

def add_task(todo_list):
    """
    Asks the user for a task and adds it to the list.
    """
    # Prompt User To Enter The Task Details
    task = input("Enter A Task To Add: ").strip()
    
    if task:
        # Append The New Task To The End Of The List
        todo_list.append(task)
        print(f"Sure {user_name}, The Task '{task}' Was Added Successfully.")
    else:
        print("Cannot Add An Empty Task!")

def view_tasks(todo_list):
    """
    Displays all tasks currently in the list with their numbers.
    """
    # Check If The List Is Empty
    if not todo_list:
        print("Opps! No Tasks To Display.")
    else:
        print(f"\n--- {user_name}'s To-Do List ---")
        # Loop Through The List And Enumerate To Show Index (Starting From 1)
        for index, task in enumerate(todo_list, start=1):
            print(f"{index} - {task}")
        print("-" * 30)

def remove_task(todo_list):
    """
    Removes a specific task based on its number.
    """
    # Check If There Is Anything To Remove First
    if not todo_list:
        print("Opps! No Tasks To Remove.")
        return

    # Show The List So The User Knows Which Number To Pick
    view_tasks(todo_list)

    try:
        # Get The Index From The User And Convert To Integer
        task_num = int(input("\nEnter The Task Number To Remove: "))

        # Validate If The Number Is Within The Range Of The List
        if 1 <= task_num <= len(todo_list):
            # Remove The Item At The Correct Index (User Input - 1)
            removed_task = todo_list.pop(task_num - 1)
            print(f"Sure {user_name}, Task '{removed_task}' Was Removed.")
        else:
            print("Invalid Number, Please Check The List Again.")

    except ValueError:
        # Handle Cases Where User Enters Text Instead Of A Number
        print("Error: Please Enter A Valid Numeric Value.")

# --------------------------------[ App Initialization ]-----------------------------------

# Clear Screen At Start
clear_screen()

print("Welcome To The To-Do List App!")
print("-" * 30)

# Get User Name And Capitalize The First Letter
user_name = input("Enter Your Name: ").strip().capitalize()
print(f"Hello, {user_name}! Let's Manage Your Tasks.")

# Initialize An Empty List To Store Tasks
todo_list = []

# --------------------------------[ Main Program Loop ]-----------------------------------

while True:
    # Get Command From User (Convert To Lowercase To Handle 'ADD', 'Add', etc.)
    user_choice = input("\nPlease Enter A Command (add, view, remove, clear, exit): ").strip().lower()

    # Route The Command To The Correct Function
    if user_choice == "add":
        add_task(todo_list)

    elif user_choice == "view":
        view_tasks(todo_list)

    elif user_choice == "remove":
        remove_task(todo_list)

    elif user_choice == "clear":
        clear_screen()
        print("Screen Cleaned! Ready For Next Command.")

    elif user_choice == "exit":
        print(f"Goodbye {user_name}, Have A Great Day!")
        # Break The Loop To End The Program
        break

    else:
        # Handle Unknown Commands
        print("Invalid Command, Please Try With Available Options.")