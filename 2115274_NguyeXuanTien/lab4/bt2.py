import tkinter as tk

root=tk.Tk()
root.geometry("250x100")
tk.title="login"
taiKhoan=tk.StringVar()
matkhau=tk.StringVar()

def xacnhan():
    tk=taiKhoan.get()
    mk=matkhau.get()

    print("Ten tai khoan: "+tk)
    print("Mat khau la: "+matkhau)

    taiKhoan.set("")
    matkhau.set("")

tk_lbl=tk.Label(root,text="Tai Khoan")
tk_entry=tk.Entry(root,textvariable= taiKhoan)
mk_lbl=tk.Label(root,text="Mat Khau")
mk_entry=tk.Entry(root, textvariable=matkhau)
xaxnhan_btn=tk.Button(root,text="Xac Nhan", command= xacnhan)

tk_lbl.grid(row=0,column=0)
tk_entry.grid(row=0,column=1)
mk_lbl.grid(row=1,column=0)
mk_entry.grid(row=1,column=1)
xaxnhan_btn.grid(row=2,column=1)

root.mainloop()