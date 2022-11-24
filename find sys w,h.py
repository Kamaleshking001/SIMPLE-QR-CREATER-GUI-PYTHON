from tkinter import *

root=Tk()

sysW=root.winfo_screenwidth()
sysH=root.winfo_screenheight()

WID=Label(root,text="WIDTH:"+str(sysW))
WID.pack()

HEI=Label(root,text="HEIGHT:"+str(sysH))
HEI.pack()