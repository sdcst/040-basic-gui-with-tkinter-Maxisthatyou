import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")


entry1 = tk.Entry(window, width=15)
label1 = tk.Label(window,text="X")
entry2 = tk.Entry(window, width=15)
button1 = tk.Button(window,text="=")
entry3 = tk.Entry(window, width=30)

entry1.pack(side=LEFT)
label1.pack(side=LEFT)
entry2.pack(side=LEFT)
button1.pack(side=LEFT)
entry3.pack(side=LEFT)

window.mainloop()