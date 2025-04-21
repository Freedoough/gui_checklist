from logging import root
import tkinter as tk
from tkinter import ttk
import math
import time


# Root window setup
root = tk.Tk()
root.title("Checklist")
root.geometry("500x800") 



# Create a label for the title
title_label = tk.Label(root, text="Checklist", font=("Arial, 24")) 
title_label.pack(pady=10) 


# Create label for task name entry box
task_name_label = tk.Label(root, text="Task Name:", font="Arial, 12")
task_name_label.pack(pady=5, anchor="w")

entry_box = tk.Entry(root, width=50)
entry_box.pack(anchor="nw") 


# Create a list of items


# Main program loop
root.mainloop()
