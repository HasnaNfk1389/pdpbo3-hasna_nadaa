from tkinter import Tk, Frame, Checkbutton, BOTH, Label

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.initUI()
        self.buatCheckButton()
        
    
    def initUI(self):
        self.parent.title("Genre")
        self.pack(fill=BOTH, expand=True)
        self.parent.geometry("200x100")

    def buatCheckButton(self):
        cb = Checkbutton(self, text="Laki-Laki")
        cb.place(x=20, y=40)

        cb = Checkbutton(self, text="Perempuan")
        cb.place(x=20, y=20)
    
    

if __name__ == '__main__':
    root = Tk()
    app = Example(root)
    root.mainloop()