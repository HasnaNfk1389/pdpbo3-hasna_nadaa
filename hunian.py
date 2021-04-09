from tkinter import *

class RadioButton(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.window = parent
        self.v = IntVar()
        
        self.teks()
        self.radioButton()
        self.tombol()

    def teks(self):
        Label(root, text="""pilih bahasa yang kalian sukai :""", justify=LEFT, padx=20).pack()

    def radioButton(self):
        Radiobutton(root, text="Indonesia", padx=20, command=self.tampilkan, variable=self.v, value=1).pack(anchor=W)
        Radiobutton(root, text="Bahasa Inggris", padx=20, variable=self.v, command=self.tampilkan, value=2).pack(anchor=W)

    def tampilkan(self):
        if self.v.get() == 1:
            print ("Bahasa Indonesia")
        elif self.v.get() == 2 :
            print ("Bahasa inggris")
    
    def tombol(self):
        tombolTutup = Button(self, text="Tutup", command=self.quit)
        tombolTutup.pack(side=RIGHT, padx=5, pady=5)
     
        tombolOke = Button(self, text="Oke", command=self.quit)
        tombolOke.pack(side=RIGHT)

if __name__ == '__main__':
    root = Tk()
    root.geometry("200x100")
    RadioButton(root)
    mainloop()