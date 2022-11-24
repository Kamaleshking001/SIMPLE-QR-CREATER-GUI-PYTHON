from tkinter import *

from centerscreen import *

import pyqrcode

root.config(bg="black")
root.resizable(0,0)
centerscr(500,500)

def create():
    new = url.get()
    url1=pyqrcode.create(new)
    url1.show(scale=8)
    new1=fname.get()
    url1.png(f'{new1}.png', scale=8)

Label(root,text="QR GENERATER",background="silver",width=28,fg="white",highlightthickness=3,font=('calibri',25,'bold')).place(x=8,y=10)


Label(root,text="ENTER URL",fg="lightblue",bg="black",font=("robot",20,"bold"),pady=5).place(x=180,y=70)
url=Entry(root,width=35,font=("times",15,"bold"),fg="white",bg="black",highlightbackground="blue",highlightthickness=2)
url.place(x=80,y=120)


Label(root,text="ENTER FILENAME:",fg="lightblue",bg="black",font=("robot",20,"bold"),pady=5).place(x=150,y=160)
fname=Entry(root,width=35,font=("times",15,"bold"),fg="white",bg="black",highlightbackground="green",highlightthickness=2)
fname.place(x=80,y=200)


Button(root,text="CREATE  &  SAVE\n.PNG file",bg="silver",font=(10),width=30,command=create).place(x=120,y=250)


root.mainloop()
