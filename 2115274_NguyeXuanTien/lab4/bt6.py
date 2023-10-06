from tkinter import *
from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Style
from tkinter.ttk import Entry

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.columnconfigure(1,pad=5)

        self.parent.title("Dang ky hoc phan")
        rong=Label(self,text="")
        rong.grid(row=0,column=0)
        thongbao=Label(self,text="THONG TIN DANG KY HOC PHAN",fg="red",font=('calibre',10,'bold'))
        thongbao.grid(row=0,column=1)
        maso_lbl=Label(self,text="Ma so sinh vien")
        maso_lbl.grid(row=1,column=0)
        maso_entry=Entry(self)
        maso_entry.grid(row=1,column=1)
        hoten_lbl=Label(self,text="Ho ten")
        hoten_lbl.grid(row=2,column=0)
        hoten_entry=Entry(self)
        hoten_entry.grid(row=2,column=1)
        nsinh_lbl=Label(self,text="Ngay Sinh")
        nsinh_lbl.grid(row=3,column=0)
        nsinh_entry=Entry(self)
        nsinh_entry.grid(row=3,column=1)
        email_lbl=Label(self,text="Email")
        email_lbl.grid(row=4,column=0)
        email_entry=Entry(self)
        email_entry.grid(row=4,column=1)
        sdt_lbl=Label(self,text="Ngay Sinh")
        sdt_lbl.grid(row=5,column=0)
        sdt_entry=Entry(self)
        sdt_entry.grid(row=5,column=1)
        hocky_lbl=Label(self,text="Hoc ky")
        hocky_lbl.grid(row=6,column=0)
        hocky_entry=Entry(self)
        hocky_entry.grid(row=6,column=1)
        namhoc_lbl=Label(self,text="Nam hoc")
        namhoc_lbl.grid(row=7,column=0)
        namhoc_entry=Entry(self)
        namhoc_entry.grid(row=7,column=1)

        
        self.pack(fill=BOTH,expand=1)
        


root = Tk()
root.geometry("400x300+300+300")
app = Example(root)
root.mainloop()