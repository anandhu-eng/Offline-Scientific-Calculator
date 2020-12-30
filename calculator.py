from tkinter import *
from PIL import Image,ImageTk

window=Tk()




#entry box
box=Entry(window,text=StringVar(),state=DISABLED)
box.grid(row=0,column=0,columnspan=3)

#functions for each button
def one():
	one=1
	print("clicked the button")

def two():
	two=2
	print("clicked the button")

def three():
	three=3
	print("clicked the button")

def four():
	four=4
	print("clicked the button")

def five():
	five=5
	print("clicked the button")

def six():
	six=6
	print("clicked the button")

def seven():
	seven=7
	print("clicked the button")

def eight():
	eight=8
	print("clicked the button")

def nine():
	nine=9
	print("clicked the button")

def zero():
	zero=0
	print("clicked the button")



#buttons
one=Button(window,text="1",command=one)
one.grid(row=1,column=0)

two=Button(window,text="2",command=two)
two.grid(row=1,column=1)

three=Button(window,text="3",command=three)
three.grid(row=1,column=2)

four=Button(window,text="4",command=four)
four.grid(row=2,column=0)

five=Button(window,text="5",command=five)
five.grid(row=2,column=1)

six=Button(window,text="6",command=six)
six.grid(row=2,column=2)

seven=Button(window,text="7",command=seven)
seven.grid(row=3,column=0)

eight=Button(window,text="8",command=eight)
eight.grid(row=3,column=1)

nine=Button(window,text="9",command=nine)
nine.grid(row=3,column=2)

zero=Button(window,text="0",command=zero)
zero.grid(row=4,column=1)

window.mainloop()