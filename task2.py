import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
dogphoto = PhotoImage(file="dog.png")

entry1 = tk.Entry(window, width=15)
label1 = tk.Label(window,text="Client Database")
label2 = tk.Label(window, image= dogphoto)
entry2 = tk.Entry(window, width=15)
button1 = tk.Button(window,text="Search by Name")
button2 = tk.Button(window,text="Save Entry", width=20, height=10, bg="#808080")
entry3 = tk.Entry(window, width=15)
entry4 = tk.Entry(window, width=15)
entry5 = tk.Entry(window, width=15)
entry6 = tk.Entry(window, width=15)
button2 = tk.Button(window,text="< Previous")
button3 = tk.Button(window,text="Next >")
label3 = tk.Label(window,text="Name")
label4 = tk.Label(window,text="Type")
label5 = tk.Label(window,text="Breed")
label6 = tk.Label(window,text="Owner")
label7 = tk.Label(window,text="Birthdate")

label2.grid(row=1, column=1, rowspan=3)
button1.grid(row=1, column=4)
entry2.grid()
button1.pack(side=LEFT)
entry3.pack(side=LEFT)

window.mainloop()