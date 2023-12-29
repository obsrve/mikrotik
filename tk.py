from tkinter import *
from tkinter import ttk

root = Tk()  # Create root object
root.title("test window")  # Title name
root.geometry("300x250")  # window size

label = Label(text="Mikrotik")  # create start point
label.pack()

root.mainloop()
