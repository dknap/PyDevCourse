import tkinter as tk                                                            # import lib
from tkinter import ttk

win = tk.Tk()                                                                   # create new object tk
win.title("Python course")                                                      # program title
win.resizable(1, 1)                                                             # turn off resizable
ttk.Label(win, text="Author: Dawid Knap").grid(column = 0,  row = 0)            # add label to grid
win.mainloop()                                                                  # display all time
