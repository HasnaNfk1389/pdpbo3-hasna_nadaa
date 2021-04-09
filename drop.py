from tkinter import *
from tkinter import Tk

root = Tk()
root.title("Dropdown")
root.geometry("400x200")

# Drop Down Boxes

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Kategori",
    "Sedang",
    "Biasa",
    "Tinggi",
    "High Class"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()