from tkinter import *
from tkinter import ttk

root = Tk()  # Create root object
root.title("test window")  # Title name
# root.geometry("300x250")  # window size


def text():
    label = Label(root, text=inp.get())
    # label.pack()
    label.grid()


inp = Entry(root, width=20, borderwidth=5)
inp.grid(row=0, column=0, padx=10, pady=10, columnspan=3)


btn = Button(root, text="Confirm", padx=15, state='active', command=text)
btn.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

root.mainloop()
