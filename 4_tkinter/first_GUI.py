import tkinter as tk                                                            # import lib
from tkinter import ttk

win = tk.Tk()                                                                   # create new object tk
win.title("Python course")                                                      # program title
win.resizable(1, 1)                                                             # turn off resizable
# ttk.Label(win, text="Author: Dawid Knap").grid(column = 0,  row = 0)            # add label to grid

#label
aLabel = ttk.Label(win, text="First label")
aLabel.grid(column=0, row=0)

#Button Click Event Function
def clickMe():
    action.configure(text="** clicked! **")
    aLabel.configure(foreground="red")
    aLabel.configure(text="Second label")

# Adding a button
action = ttk.Button(win, text="--> Click <--", command=clickMe)
action.grid(column=0, row=1)

win.mainloop()                                                                  # display all time
