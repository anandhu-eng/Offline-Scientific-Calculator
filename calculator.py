from tkinter import *
from PIL import Image,ImageTk

window=Tk()




#entry box
box=Entry(window,text=StringVar())
box.grid(row=0,column=0,columnspan=3)


#buttons
one=Button(window,text="1")
one.grid(row=1,column=0)

two=Button(window,text="2")
two.grid(row=1,column=1)

three=Button(window,text="3")
three.grid(row=1,column=2)

four=Button(window,text="4")
four.grid(row=2,column=0)

five=Button(window,text="5")
five.grid(row=2,column=1)

six=Button(window,text="6")
six.grid(row=2,column=2)

seven=Button(window,text="7")
seven.grid(row=3,column=0)

eight=Button(window,text="8")
eight.grid(row=3,column=1)

nine=Button(window,text="9")
nine.grid(row=3,column=2)

zero=Button(window,text="0")
zero.grid(row=4,column=1)

window.mainloop()