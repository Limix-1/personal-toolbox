import tkinter as tk
from tkinter import *


root = tk.Tk()
sb = Scrollbar(root)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(root, yscrollcommand=sb.set)

for i in range(1000):
    lb.insert(END, str(i))

lb.pack(side=LEFT, fill=BOTH)

sb.config(command=lb.yview)

root.mainloop()