from tkinter import *

window = Tk()
window.title("lil mischif")
# window.minsize(500, 300)

# top title for app
title_label = Label(text="miles to kilometers", font=("Arial", 16))
title_label.grid(row=0)


def button_clicked():
    text = input.get()
    title_label.configure(text=text)
    button.config(text="you pressed this")


button = Button(text="Click Me", command=button_clicked)
button.grid(row=1)

input = Entry()
input.grid(row=2)

window.mainloop()
