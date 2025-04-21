from logging import root
import tkinter as tk
from tkinter import ttk
import math
import time



root = tk.Tk()
root.title("Checklist")

# Create a frame for the checklist
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
