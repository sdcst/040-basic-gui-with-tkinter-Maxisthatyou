import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
dogphoto = PhotoImage(file="dog.png")
window.geometry("260x135")

label3 = tk.Label(window, image=dogphoto)
label1 = tk.Label(window,text="A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero", bg="#00FFFF")
label2 = tk.Label(window,text="Ponchacco!")

label3.place(x=66.6667, y=0)
label1.place(x=0, y=100)
label2.place(x=135, y=33.333)


window.mainloop()