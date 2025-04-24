from logging import root
import tkinter as tk
from tkinter import ttk
import math
import time


# Root window setup
root = tk.Tk()
root.title("Checklist")
root.geometry("700x600") 

# Function to add task to listbox
def add_task():
    task_entry_label.config(text=entry_box.get())


# Enter button widget
enter_button = tk.Button(
    root, 
    text="Enter", 
    font="Arial, 12", 
    command=lambda: add_task(), 
    justify="right"
    )
enter_button.grid(row=1, column=2, padx=1, pady=1)

# Title label
title_label = tk.Label(root, text="Checklist", font=("Arial, 24"), justify="center") 
title_label.grid(row=0, column=1, pady=5) 


# Task name label next to entry box
task_name_label = tk.Label(root, text="Task Name:", font="Arial, 12", justify="left")
task_name_label.grid(row=3, column=0, padx=1, pady=5)


# Entry box
entry_box = tk.Entry(root, width=50, justify="center")
entry_box.grid(row=3, column=1, padx=1, pady=5)





# Listbox label
task_entry_label = tk.Label(root, text="Tasks" , font="Arial, 12", justify="left")
task_entry_label.grid(row=6, column=0, pady=3)


# Listbox for entered tasks
task_listbox = tk.Listbox(root, width=30, height=20, justify="left")
task_listbox.grid(row=8, column=0, padx=6, pady=5)


# Completed tasks listbox label
completed_tasks_label = tk.Label(root, text="Completed Tasks", font="Arial, 12", justify="right")
completed_tasks_label.grid(row=6, column=2, pady=3)

# Listbox for completed tasks
completed_tasks_lebel = tk.Listbox(root, width=30, height=20, justify="right")
completed_tasks_lebel.grid(row=8, column=2, padx=2, pady=5)


# Clear all button widget

clear_button = tk.Button(root, text="Clear all", font="Arial, 12", command=lambda: task_listbox.delete(0, tk.END), justify="center")
    
clear_button.grid(row=9, column=1, padx=0, pady=0)

# Main program loop
root.mainloop()
