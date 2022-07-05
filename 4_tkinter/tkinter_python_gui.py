import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from webbrowser import BackgroundBrowser

win = tk.Tk()
win.title('TextBoxWidget')

#label
# aLabel = ttk.Label(win, text='First label')
# aLabel.grid(column=0, row=0)

# button modification
def clickMe():
    action.configure(text='Hello, ' + name.get() + '! Your number: ' + numberChosen.get())

# change label
aLabel = ttk.Label(win, text='Enter a name:' ).grid(column=0, row=0)
# aLabel.configure(text='Enter a name: ')

# add textbox
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# add button
action = ttk.Button(win, text='--> Clik me <--', command=clickMe)
action.grid(column=1, row=1)
# action.configure(state='disable')
nameEntered.focus()

# ComboBox
ttk.Label(win, text='Choose number: ').grid(column=0, row=3)
number = tk.StringVar
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=3)
numberChosen.current(0)

# Checkbox - disabled
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

# Checkbox - Unchecked
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

# Checkbox - Checked
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


# RadioButton

# color1 = 'Red'
# color2 = 'Green'
# color3 = 'Blue'

colors = ['Red', 'Green', 'Blue']

# def radCall():
#     radSel = radVar.get()
#     if radSel == 1: win.configure(background=color1)
#     elif radSel == 2: win.configure(background=color2)
#     elif radSel == 3: win.configure(background=color3)

def radCall():
    radSel = radVar.get()
    if radSel == 0: win.configure(background=colors[radSel])
    elif radSel == 1: win.configure(background=colors[radSel])
    elif radSel == 2: win.configure(background=colors[radSel])


radVar = tk.IntVar()
radVar.set(99)

# rad1 = tk.Radiobutton(win, text=color1, variable=radVar, value=1, command=radCall)
# rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

# rad2 = tk.Radiobutton(win, text=color2, variable=radVar, value=2, command=radCall)
# rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

# rad3 = tk.Radiobutton(win, text=color3, variable=radVar, value=3, command=radCall)
# rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

for col in range(len(colors)):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)


# ScrolledText

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3)


# Label Frame

labelsFrame = ttk.LabelFrame(win, text=' --- Labels in Frame ---')
labelsFrame.grid(column=0, row=8, padx=10, pady=10)     # in px

ttk.Label(labelsFrame, text='Label1').grid(column=0, row=0)
ttk.Label(labelsFrame, text='Label2').grid(column=0, row=1)
ttk.Label(labelsFrame, text='Label3').grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=10, pady=10)


win.mainloop()
