import tkinter as tk
import ttkbootstrap as ttk
from tkinter import ttk


def button_func():
    print("TEXXXXT AHHHHHH")


window = tk.Tk()
window.title("windowsAndWidgets")
window.geometry("800x500")

# basic label
label = tk.Label(master=window, text="LABEL AHHH").pack()

# basic text widget
text = tk.Text(master=window).pack()

# basic entry widget
entry = ttk.Entry(master=window).pack()

# basic button
button = ttk.Button(master=window, text=" A Button", command=button_func)

# basic
button

# run command
window.mainloop()
