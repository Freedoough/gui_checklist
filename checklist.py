from logging import root
import tkinter as tk
from tkinter import ttk
import math
import time


# Root window setup
root = tk.Tk()
root.title("Checklist")
root.geometry("500x800") 


# # Create label for task name entry box
# task_name_label = tk.Label(root, text="Task Name:", font="Arial, 12")
# task_name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# # Create an entry box for task name
# entry_box = tk.Entry(root, width=50, justify="center")
# entry_box.grid(row=0, column=1, padx=5, pady=5)





# Create a label for the title
title_label = tk.Label(root, text="Checklist", font=("Arial, 24")) 
title_label.pack(pady=10) 


# Create label for task name entry box
task_name_label = tk.Label(root, text="Task Name:", font="Arial, 12")
task_name_label.pack(pady=5, anchor="w")

# Create an entry box for task name
entry_box = tk.Entry(root, width=50, justify="center")
entry_box.pack() 

# Create a label for task entry box
task_entry_label = tk.Label(root, text="Tasks" , font="Arial, 12")
task_entry_label.pack(pady=5, anchor="w")





# Create a list of items


# Main program loop
root.mainloop()
