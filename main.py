from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, RAISED
from tkinter.ttk import Frame, Label, Entry, Button


class membuatKomentar(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()

    def initUI(self):
        self.window.title("Main Window")
        self.pack(fill=BOTH, expand=True)
        

        self.elemen1()
        self.elemen2()
        self.elemen3()
        self.tombol()
               
    def elemen1(self) :
        teksField1 = Frame(self)
        teksField1.pack(fill=X)

        teks1 = Label(teksField1, text="Nama :", width=8)
        teks1.pack(side=LEFT, padx=5, pady=5)

        masukkanKeWindow1 = Entry(teksField1)
        masukkanKeWindow1.pack(fill=X, padx=5, expand=True)
     
    def elemen2(self):
        teksField2 = Frame(self)
        teksField2.pack(fill=X)

        teks2 = Label(teksField2, text="Umur :", width=8)
        teks2.pack(side=LEFT, padx=5, pady=5)

        masukkanKeWindow2 = Entry(teksField2)
        masukkanKeWindow2.pack(fill=X, padx=5, expand=True)
 
    def elemen3(self):
        teksField3 = Frame(self)
        teksField3.pack(fill=X)

        teks3 = Label(teksField3, text="Alamat :", width=8)
        teks3.pack(side=LEFT, padx=5, pady=5)

        masukkanKeWindow3 = Entry(teksField3)
        masukkanKeWindow3.pack(fill=X, padx=5, expand=True)
 
    def tombol(self):
        tombolTutup = Button(self, text="Tutup", command=self.quit)
        tombolTutup.pack(side=RIGHT, padx=5, pady=5)
     
        tombolOke = Button(self, text="Oke", command=self.quit)
        tombolOke.pack(side=RIGHT)


if __name__ == '__main__':
    root = Tk()
    root.geometry("400x200")
    app = membuatKomentar(root)
    root.mainloop()