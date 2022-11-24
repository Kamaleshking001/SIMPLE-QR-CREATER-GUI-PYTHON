from tkinter import *

root=Tk()

def centerscr(w,h):
    sysW = root.winfo_screenwidth()
    sysH = root.winfo_screenheight()

    x=(sysW/2)-(w/2)
    y=(sysH/2)-(h/2)
    root.geometry("%dx%d+%d+%d" % (w,h,x,y))