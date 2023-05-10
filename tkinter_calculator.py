
#popupular frameworks Tkinter, Kivy, PyQt5, Pygame
from tkinter import *

main_layout= Tk() #the window

Label(main_layout, text= "Scientific Calculator"). grid(row=0, column= 1, columnspan=4)

screen= Entry(main_layout,width=30, borderwidth=10)
screen.grid(row=1, column=1, columnspan=4)

#getting numbers
def calculations(number):
    #screen.delete(0,END) #deletes whats already in the screen
    current_value= screen.get()
    screen.delete(0,END)
    screen.insert(0, str(current_value)+ str(number)) #insert the number pressed in the screen
    
#clearing the screen
def clearing():
    screen.delete(0,END)
    
contents = []

def add ():
    first_n= screen.get() 
    #cant initialize and assign a global variable on 1 line??
    global num1 
    num1 = int(first_n)
    contents.append(num1)
    contents. append('+')
    screen.delete(0, END)
    
def subtract ():
    first_n= screen.get() 
    #cant initialize and assign a global variable on 1 line??
    global num1 
    num1 = int(first_n)
    contents.append(num1)
    contents. append('-')
    screen.delete(0, END)
    
def divide ():
    first_n= screen.get() 
    #cant initialize and assign a global variable on 1 line??
    global num1 
    num1 = int(first_n)
    contents.append(num1)
    contents. append('/')
    screen.delete(0, END)
    
def multiplying ():
    first_n= screen.get() 
    #cant initialize and assign a global variable on 1 line??
    global num1 
    num1 = int(first_n)
    contents.append(num1)
    contents. append('*')
    screen.delete(0, END)
    
def equals():
    second_n= screen.get()
    contents.append(second_n)
    screen.delete(0,END)
    if contents[1]=='+':
        screen.insert(0,num1 + int(second_n)) 
    if contents[1]=='-':
        screen.insert(0,num1 - int(second_n))
    if contents[1]=='*':
        screen.insert(0,num1 * int(second_n))
    if contents[1]=='/':
        screen.insert(0,num1 / int(second_n))
    contents.clear()

#first row of numbers
press7= Button(main_layout, text= '7', command = lambda: calculations(7))
press7.grid(row=3, column= 1, padx= 10, pady=10)#putting it on the screen

press8= Button(main_layout, text= '8', command = lambda: calculations(8))
press8.grid(row=3, column= 2, padx= 10, pady=10)#can increase the button size by increasing the pad

press9= Button(main_layout, text= '9', command = lambda: calculations(9))
press9.grid(row=3, column= 3, padx= 10, pady=10)

clear_button= Button(main_layout, text= 'Del', command = clearing)#used lambda cause need to pass argument
clear_button.grid(row=3, column= 4, padx= 5, pady=5)

#second row of numbers
press4= Button(main_layout, text= '4', command =lambda: calculations(4))
press4.grid(row=4, column= 1, padx= 10, pady=10)

press5= Button(main_layout, text= '5', command = lambda: calculations(5))
press5.grid(row=4, column= 2, padx= 10, pady=10)

press6= Button(main_layout, text= '6', command = lambda: calculations(6))
press6.grid(row=4, column= 3, padx= 10, pady=10)

multiply= Button(main_layout, text= 'x', command = multiplying)
multiply.grid(row=4, column= 4, padx= 5, pady=5)

#third row of numbers
press1= Button(main_layout, text= '1', command = lambda: calculations(1))
press1.grid(row=5, column= 1, padx= 10, pady=10)

press2= Button(main_layout, text= '2', command = lambda: calculations(2))
press2.grid(row=5, column= 2, padx= 5, pady=5)

press3= Button(main_layout, text= '3', command = lambda: calculations(3))
press3.grid(row=5, column= 3, padx= 10, pady=10)

division= Button(main_layout, text= '/', command = divide)
division.grid(row=5, column= 4, padx= 5, pady=5)

#Fourth row of numbers
press0= Button(main_layout, text= '0',command = lambda: calculations(0))
press0.grid(row=6, column= 1, padx= 10, pady=10)

plus= Button(main_layout, text= '+', command = add)
plus.grid(row=6, column= 2, padx= 5, pady=5)

minus= Button(main_layout, text= '-', command = subtract)
minus.grid(row=6, column= 3, padx= 5, pady=5)

answer= Button(main_layout, text= '=', command = equals)
answer.grid(row=6, column= 4, padx= 5, pady=5)


main_layout.mainloop() #event loop, it is a constant loop