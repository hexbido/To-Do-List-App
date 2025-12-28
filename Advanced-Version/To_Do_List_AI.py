import tkinter as tk
from tkinter import messagebox
import os

# --------------------------------[ Configuration & Themes ]-----------------------------------

# Define Application Colors (Dark Theme Palette)
BG_MAIN  = "#1e1e1e"      # Dark Background
BG_SEC   = "#252526"      # Slightly Lighter Background For Inputs
FG_TEXT  = "#d4d4d4"      # Light Grey Text
BTN_BLUE = "#007acc"      # Visual Studio Blue
BTN_GOLD = "#d7ba7d"      # Gold For 'Done' Status
BTN_RED  = "#f44747"      # Red For Deletion
SUCCESS  = "#7cb462"      # Green Color For Completed Tasks

# Define Window Dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 470

# --------------------------------[ App Initialization ]-----------------------------------

# Initialize The Main Window
root = tk.Tk()
root.title("Bido To-Do List 📝")
root.configure(bg=BG_MAIN)

# Calculate Screen Center To Position The Window Perfectly
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_pos = (screen_width // 2) - (WINDOW_WIDTH // 2)
y_pos = (screen_height // 2) - (WINDOW_HEIGHT // 2)

# Apply Geometry (Size + Position)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x_pos}+{y_pos}")

# --------------------------------[ Data Management ]-----------------------------------

# Load Existing Tasks From File If It Exists
tasks = []
if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file.readlines()]

# --------------------------------[ Core Functions ]-----------------------------------

def save_and_update():
    """
    Saves tasks to the file and refreshes the UI listbox.
    """
    # Clear The Current List In The UI
    listbox.delete(0, tk.END)

    # Loop Through Tasks To Display Them
    for task in tasks:
        # Insert Task Into Listbox
        listbox.insert(tk.END, task)
        
        # If Task Is Marked As Done (Contains Checkmark), Change Color To Green
        if "✔" in task:
            listbox.itemconfig(tk.END, fg=SUCCESS)

    # Save The Updated List To The Text File
    with open("tasks.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(tasks))

def add_task(event=None):
    """
    Adds a new task from the entry box to the list.
    """
    task_text = entry.get().strip()
    
    if task_text:
        # Add Task To List And Clear Input Field
        tasks.append(task_text)
        entry.delete(0, tk.END)
        save_and_update()
    else:
        # Show Warning If Input Is Empty
        messagebox.showwarning("Warning", "You Must Enter A Task First!")

def delete_task(event=None):
    """
    Deletes the currently selected task.
    """
    try:
        # Get Index Of Selected Item
        selected_index = listbox.curselection()[0]
        
        # Remove From List And Update UI
        del tasks[selected_index]
        save_and_update()
        
    except IndexError:
        messagebox.showinfo("Info", "Please Select A Task To Delete.")

def toggle_done():
    """
    Marks a task as complete or incomplete (Adds/Removes Checkmark).
    """
    try:
        idx = listbox.curselection()[0]
        current_task = tasks[idx]

        # Toggle Logic: Remove Checkmark If Exists, Add If Not
        if "✔" in current_task:
            tasks[idx] = current_task.replace("✔ ", "")
        else:
            tasks[idx] = f"✔ {current_task}"
            
        save_and_update()

    except IndexError:
        messagebox.showinfo("Info", "Please Select A Task To Mark As Done.")

# --------------------------------[ UI Components ]-----------------------------------

# 1. Header Label
tk.Label(root, text="My List 📝", font=("Consolas", 18, "bold"), 
         bg=BG_MAIN, fg=FG_TEXT).pack(pady=20)

# 2. Input Field (Entry)
entry = tk.Entry(root, font=("Consolas", 13), bg=BG_SEC, fg=FG_TEXT, 
                 insertbackground=FG_TEXT, relief="flat", bd=5)
entry.pack(pady=5, padx=25, fill="x", ipady=3)

# Bind 'Enter' Key To Add Task Function
entry.bind('<Return>', add_task)

# 3. Task List (Listbox)
listbox = tk.Listbox(root, font=("Consolas", 12), bg=BG_SEC, fg=FG_TEXT, 
                     height=12, selectbackground="#264f78", 
                     highlightthickness=0, relief="flat")
listbox.pack(pady=15, padx=25, fill="both", expand=True)

# 4. Buttons Container (Frame)
btn_frame = tk.Frame(root, bg=BG_MAIN)
btn_frame.pack(pady=20)

# Helper Function To Create Styled Buttons
def create_btn(text, command, color):
    btn = tk.Button(btn_frame, text=text, command=command, bg=color, fg="white", 
                    font=("Segoe UI", 10, "bold"), relief="flat", width=10, cursor="hand2")
    btn.pack(side="left", padx=5)
    return btn

# Create The Three Main Buttons
create_btn("ADD", add_task, BTN_BLUE)
create_btn("DONE", toggle_done, BTN_GOLD)
create_btn("DELETE", delete_task, BTN_RED)

# Bind 'Delete' Key To Delete Function
root.bind('<Delete>', delete_task)

# --------------------------------[ Main Loop ]-----------------------------------

# Load Data On Startup
save_and_update()

# Run The Application
root.mainloop()