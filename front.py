from tkinter import *
from tkinter import ttk
from back import url

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="adis").grid(column=2, row=3)
ttk.Button(frm, text=url, command=root.destroy).grid(column=1, row=0)
root.mainloop()