from tkinter import *

window = Tk()
window.title("Calculator")

#iconphoto
photo = PhotoImage(file="calacimg.png")
window.iconphoto(False, photo)

e = Entry(window, width=27, borderwidth=4)
e.grid(row=0, column=0, columnspan=4, padx=0, pady=0, ipady=20)

#button fuctions

def button_click(number):
    #e.delete(0, END)
    current_val = e.get()
    e.delete(0, END)
    e.insert(0, str(current_val) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    fisrt_number = e.get()
    global f_num
    global math
    math = "Addition"
    f_num = float(fisrt_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "Addition":
        e.insert(0, f_num + float(second_number))
    if math == "Multiplication":
        e.insert(0, f_num * float(second_number))
    if math == "Division":
        e.insert(0, f_num / float(second_number))
    if math == "Substraction":
        e.insert(0, f_num - float(second_number))



def button_substract():
    fisrt_number = e.get()
    global f_num
    global math
    math = "Substraction"
    f_num = float(fisrt_number)
    e.delete(0, END)

def button_multiply():
    fisrt_number = e.get()
    global f_num
    global math
    math = "Multiplication"
    f_num = float(fisrt_number)
    e.delete(0, END)

def button_divide():
    fisrt_number = e.get()
    global f_num
    global math
    math = "Division"
    f_num = float(fisrt_number)
    e.delete(0, END)



# define buttons

button_1 = Button(window, text="1", padx=20, pady=10, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=20, pady=10, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=20, pady=10, command=lambda: button_click(3))

button_4 = Button(window, text="4", padx=20, pady=10, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=20, pady=10, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=20, pady=10, command=lambda: button_click(6))

button_7 = Button(window, text="7", padx=20, pady=10, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=20, pady=10, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=20, pady=10, command=lambda: button_click(9))

button_0 = Button(window, text="0", padx=19, pady=10, command=lambda: button_click(0))
button_dot = Button(window, text=".", padx=21, pady=10, command=lambda: button_click('.'))
button_equal = Button(window, text="=", padx=19, pady=10, command=button_equal)

button_clear = Button(window, text="CLR", padx=12, pady=10, command=button_clear)
button_divide = Button(window, text="/", padx=20, pady=10, command=button_divide)

button_multiply = Button(window, text="X", padx=19, pady=10, command=button_multiply)

button_substract = Button(window, text="-", padx=20, pady=10, command=button_substract)
button_add = Button(window, text="+", padx=18, pady=10, command=button_add)

button_tan=Button(window, text="tan", padx=14, pady=10)
button_cos=Button(window, text="cos", padx=14, pady=10)
button_sin=Button(window, text="sin", padx=14, pady=10)




#put buttons on the display

button_clear.grid(row=5, column=2)
button_divide.grid(row=1, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_substract.grid(row=3, column=3)


button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_0.grid(row=5, column=1)
button_equal.grid(row=5, column=3)
button_dot.grid(row=5, column=0)

button_tan.grid(row=1,column=0)
button_sin.grid(row=1,column=1)
button_cos.grid(row=1,column=2)





window.mainloop()