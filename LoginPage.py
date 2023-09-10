import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter
import coreProgram
#load image for front-end
base=tkinter.Tk()
background=PhotoImage(file='back.png')
signfont=PhotoImage(file='sign.png')
fontuser=PhotoImage(file='user.png')
fontpass=PhotoImage(file='pass.png')
textboxuser=PhotoImage(file='entry.png')
textboxpass=PhotoImage(file='entry.png')
buttonlog=PhotoImage(file='button.png')
showbox=PhotoImage(file='showpass.png')
fontshow=PhotoImage(file='fontshow.png')
#set variable private
nameData='Guplation'
passData='admin123'
temp=IntVar(value=0)
e1_str=tk.StringVar()

class logForm():
    def __init__(self, parent):
        self.parent=parent
        self.parent.title("Guplation")
        self.myCanvas()
        self.myEntry()
        self.myButton()
def myCanvas(self):
    global canvas
    canvas=Canvas(self.parent, width=600, height=400, bg='white')
    canvas.create_image(160,200, image=background)
    canvas.create_image(430, 100, image=signfont)
    canvas.create_image(340, 180, image=fontuser)
    canvas.create_image(460, 185, image=textboxuser)
    canvas.create_image(320, 230, image=fontpass)
    canvas.create_image(460,235, image=textboxpass)
    canvas.create_image(453, 253, image=fontshow )
    canvas.create_image(425, 310, image=buttonlog)
    canvas.pack()

def myEntry(self):
    global entryUser, entryPass
    entryUser=Entry(self.parent, bg="#ecf0ef", relief='flat')
    canvas.create_window(450,170, window=entryUser)
    entryPass=Entry(self.parent, bg='#ecf0ef', show="*",relief='flat',
    textvariable=e1_str)
    canvas.create_window(450, 223, window=entryPass)

def myProces(self):
    global inUser, inPass
    inUser=entryUser.get()
    inPass=entryPass.get()
    try:
     if inUser==nameData and inPass==passData:
        messagebox.showinfo('information', 'Succesful to login')
        self.parent.destroy()
        coreProgram.mainProgram()
     else:
        messagebox.showwarning('warning', 'Failed to login')
    except ValueError:
        return None

def myShow(self):
    if temp.get()==1: #temp=1 saat checklis button on
        entryPass.config(show='')
    else:
        entryPass.config(show='*')
def myButton(self):
#login button
    logx=Button(self.parent, height=50, background="white",
    width=90,relief='flat',
    image=buttonlog, takefocus=0,borderwidth=0,activebackground="white", command=self.myProces)
    canvas.create_window(425, 310, window=logx)
#shows password button
    spx=Checkbutton(self.parent,width=1,
    height=1,relief='flat', bg='white', variable=temp, onvalue=1,offvalue=0 ,command=self.myShow)
    canvas.create_window(390,255, window=spx)
    log=logForm(base)
    base.resizable(FALSE, FALSE)
    base.mainloop()



