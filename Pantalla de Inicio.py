from tkinter import*
from tkinter import messagebox
top=Tk()
c=Canvas(top,bg="blue",height=250,width=300)
fn=PhotoImage(file='maxresdefault.pgm')
backlabel=Label(top, image=fn)
backlabel.place(x=0, y=0, relwidth=1,relheight=1)

c.pack()
top.mainloop
