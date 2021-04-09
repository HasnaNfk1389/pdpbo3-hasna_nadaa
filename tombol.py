from tkinter import *

root = Tk()
root.geometry("400x200")

def btn():
    myLabel = Label(root)
    myLabel.pack()

myButton1 = Button(root, text="see all submissons", command=btn, fg="black")
myButton1.pack()

myButton2 = Button(root, text="clear all submissons", command=btn, fg="black")
myButton2.pack()

myButton3 = Button(root, text="about", command=btn, fg="black")
myButton3.pack()
root.mainloop()