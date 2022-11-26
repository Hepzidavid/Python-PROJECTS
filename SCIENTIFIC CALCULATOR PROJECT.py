from tkinter import *
from math import *

window=Tk()
window.geometry("555x620")
window.title("Scientific Calculator")


def answer(event):
    value=event.widget.cget('text')
    if value == 'clr':         #set- store multiple items in a single variable
        blank.set(' ')    #Used to set and change the value stored within a Variable
    elif value == '=':
        try:
            blank.set(eval(screen.get()))
            screen.update()    #updating and processing all the events
        except:
            blank.set('Error')
            screen.update()    
    else:
        blank.set(f'{blank.get()}{value}')


blank = StringVar()
screen = Entry(window, text=blank, font='times 35 bold', fg='black', bg='white', bd=10,justify=RIGHT)
screen.insert(0,"0")
screen.pack(pady=30)

f=Frame(window)
f.pack()
b1=Button(f,text='7',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b2=Button(f,text='8',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b3=Button(f,text='9',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b4=Button(f,text='*',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='sin',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='(',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',answer)
b2.bind('<Button-1>',answer)  #For each widget,it's possible to bind any Python functions and methods to an event
b3.bind('<Button-1>',answer)  # bind a keyboard key to handle certain events for the button widget
b4.bind('<Button-1>',answer)
b5.bind('<Button-1>',answer)
b6.bind('<Button-1>',answer)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=1, column=i)
    count += 1

f=Frame(window)
f.pack()
b1=Button(f,text='4',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b2=Button(f,text='5',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b3=Button(f,text='6',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b4=Button(f,text='-',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='cos',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text=')',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',answer)
b2.bind('<Button-1>',answer)
b3.bind('<Button-1>',answer)
b4.bind('<Button-1>',answer)
b5.bind('<Button-1>',answer)
b6.bind('<Button-1>',answer)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=2, column=i)
    count += 1

f=Frame(window)
f.pack()
b1=Button(f,text='1',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b2=Button(f,text='2',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b3=Button(f,text='3',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b4=Button(f,text='+',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='tan',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='%',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',answer)
b2.bind('<Button-1>',answer)
b3.bind('<Button-1>',answer)
b4.bind('<Button-1>',answer)
b5.bind('<Button-1>',answer)
b6.bind('<Button-1>',answer)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=3, column=i)
    count += 1

f=Frame(window)
f.pack()
b1=Button(f,text='.',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b2=Button(f,text='0',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b3=Button(f,text='sinh',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b4=Button(f,text='cosh',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b5=Button(f,text='tanh',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='pi',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)

b1.bind('<Button-1>',answer)
b2.bind('<Button-1>',answer)
b3.bind('<Button-1>',answer)
b4.bind('<Button-1>',answer)
b5.bind('<Button-1>',answer)
b6.bind('<Button-1>',answer)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=4, column=i)
    count += 1

f=Frame(window)
f.pack()
b1=Button(f,text='log10',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b2=Button(f,text='exp',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='pink', width=3)
b3=Button(f,text='/',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b4=Button(f,text='clr',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='lime green', width=3)
b5=Button(f,text='log',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='powder blue', width=3)
b6=Button(f,text='=',font='times 15 bold', padx=20, pady=20, bd=3, fg='black', bg='lime green', width=3)

b1.bind('<Button-1>',answer)
b2.bind('<Button-1>',answer)
b3.bind('<Button-1>',answer)
b4.bind('<Button-1>',answer)
b5.bind('<Button-1>',answer)
b6.bind('<Button-1>',answer)
buttons=[b1,b2,b3,b4,b5,b6]
count=0
for i in range(6):
    buttons[count].grid(row=5, column=i)
    count += 1


window.mainloop()