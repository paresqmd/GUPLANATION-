import tkinter
from tkinter import *
import pandas as pd
from sklearn import tree
import katalog

def mainProgram():
    global nitro, fost, kals, tempt, humty, phentry, rainfall, radix, restbox, mainCanvas
    global buttonrec, imgclose, imgnext
    #callback function submenu
    radix=tkinter.Tk()
    radix.geometry("500x500")
    radix.title("Main Program")
    #load image from source
    side=PhotoImage(file='side.png')
    shadow=PhotoImage(file='shadow.png')
    rightside=PhotoImage(file='rightside.png')
    titlefont=PhotoImage(file='titlefont.png')
    abcd=PhotoImage(file='abcd2.png')
    textentry=PhotoImage(file='textentry.png')
    buttonrec=PhotoImage(file='buttonrec.png')
    resultbox=PhotoImage(file='resultbox.png')
    imgclose=PhotoImage(file='imgclose.png')
    imgnext=PhotoImage(file='imgnext.png')
    #front-end layout
    mainCanvas=Canvas(radix, width=500, height=500, bg='white')
    mainCanvas.create_image(10,250, image=side)
    mainCanvas.create_image(480,40, image=shadow)
    mainCanvas.create_image(540, 300, image=rightside)
    mainCanvas.create_image(235, 140, image=titlefont)
    mainCanvas.create_image(197,243, image=abcd)
    mainCanvas.create_image(355, 125, image=textentry)
    mainCanvas.create_image(355, 155, image=textentry)
    mainCanvas.create_image(355, 188, image=textentry)
    mainCanvas.create_image(355, 220, image=textentry)
    mainCanvas.create_image(355, 255, image=textentry)
    mainCanvas.create_image(355, 295, image=textentry)
    mainCanvas.create_image(355, 335, image=textentry)
    mainCanvas.create_image(365, 385, image=resultbox)
    #entrybox
    nitro=Entry(radix, bg='#d9dad9', relief='flat')
    nitro.place(x=290, y=100, width=120, height=15)
    fost=Entry(radix, bg='#d9dad9', relief='flat')
    fost.place(x=290, y=130, width=120, height=15)
    kals=Entry(radix, bg='#d9dad9', relief='flat')
    kals.place(x=290, y=163, width=120, height=15)
    tempt=Entry(radix, bg='#d9dad9', relief='flat')
    tempt.place(x=290, y=195, width=120, height=15)
    humty=Entry(radix, bg='#d9dad9', relief='flat')
    humty.place(x=290, y=230, width=120, height=15)
    phentry=Entry(radix, bg='#d9dad9', relief='flat')
    phentry.place(x=290, y=270, width=120, height=15)
    rainfall=Entry(radix, bg='#d9dad9', relief='flat')
    rainfall.place(x=290, y=310, width=120, height=15)
    restbox=Entry(radix, bg='#d9dad9', relief='flat')
    restbox.place(x=300, y=365, width=120, height=20)

def compute():
    x1=nitro.get()
    x2=fost.get()
    x3=kals.get()
    x4=tempt.get()
    x5=humty.get()
    x6=phentry.get()
    x7=rainfall.get()
    #slicing data
    df=pd.read_csv('Crop_recommendation.csv', delimiter=',')
    subdf1=df.loc[:,['N', 'P', 'K', 'temperature','humidity', 'ph','rainfall']]
    subdf2=df.loc[:,['label']]
    parameter=subdf1.to_numpy()
    target=subdf2.to_numpy()
    #procces
    methods=tree.DecisionTreeClassifier()
    #trainingdata
    ziber=methods.fit(parameter, target)
    try:
        restbox.delete(0, END)
        ans=ziber.predict([[float(x1), float(x2), float(x3), float(x4),float(x5), float(x6),float(x7)]])
        restbox.insert(0, ans)
    except ValueError:
        return None

def close():
    radix.destroy()

def next():
    radix.destroy()
katalog.catalogy()

#button
rec=Button(radix, image=buttonrec, width=90, height=70,
background='white',borderwidth=0, relief='flat', activebackground='white',
command=compute)

mainCanvas.create_window(160, 390, window=rec)
nextB=Button(radix,image=imgnext, width=66, height=72,
background='white', borderwidth=0, relief='flat',
activebackground='white', command=next)
mainCanvas.create_window(445, 490, window= nextB)
closeBut=Button(radix, image=imgclose, background='white',
width=58, height=72,
activebackground='white', relief='flat', borderwidth=0, command=close)
mainCanvas.create_window(140,490, window=closeBut)
mainCanvas.pack()
radix.resizable(FALSE, FALSE)
radix.mainloop()

