from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12, 5), facecolor='white')
axis = fig.add_subplot(111)

xValues = [0, 5, 10, 15]
yValues0 = [5.7, 7.5, 6.6, 9]
yValues1 = [5.5, 6.5, 8.5, 9]
yValues2 = [6.5, 7.1, 8.7, 9]

t0, = axis.plot(xValues, yValues0, color='red')
t1, = axis.plot(xValues, yValues1, color='green')
t2, = axis.plot(xValues, yValues2, color='blue' )

axis.set_xlabel('Horizontal Label')
axis.set_ylabel('Vertical Label')

axis.grid(linestyle='dashed')

fig.legend((t0, t1, t2), ('First line', 'Second line', 'Third line'), 'upper right')

def _destroyWindows():
    root.quit()
    root.destroy()

root = tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindows)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()
root.mainloop()