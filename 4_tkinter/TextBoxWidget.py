import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("TextBoxWidget")

#label
# aLabel = ttk.Label(win, text="First label")
# aLabel.grid(column=0, row=0)

# button modification
def clickMe():
    action.configure(text="Hello " + name.get())

# change label
aLabel = ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
# aLabel.configure(text="Enter a name: ")

# add textbox
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# add button
action = ttk.Button(win, text="--> Clik me <--", command=clickMe)
action.grid(column=1, row=1)

win.mainloop()