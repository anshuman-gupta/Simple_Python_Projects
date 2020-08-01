from tkinter import *

root = Tk()


root.title("Calculator")

Label1 = Label(root, text="CALCULATOR")
Label1.grid(row=0, columnspan=20)


equa = ""
equation = StringVar()

calculation = Entry(root, textvariable=equation,relief=RIDGE,justify='right', bd=20, bg="powder blue",font='arial 20 bold')

equation.set("")

calculation.grid(row=1, columnspan=8)

def ailachu():
    global equa
    equa = equa + str("ANSHUMAN")
    equation.set(equa)



def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)


def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""


def ClearPress():
    global equa
    equa = ""
    equation.set("")


Button0 = Button(root, text="0", command=lambda: btnPress(0), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button0.grid(row=6, column=2,padx=10,pady=10)
Button1 = Button(root, text="1", command=lambda: btnPress(1), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button1.grid(row=3, column=1,padx=10,pady=10)
Button2 = Button(root, text="2", command=lambda: btnPress(2), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button2.grid(row=3, column=2,padx=10,pady=10)
Button3 = Button(root, text="3", command=lambda: btnPress(3), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button3.grid(row=3, column=3,padx=10,pady=10)
Button4 = Button(root, text="4", command=lambda: btnPress(4), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button4.grid(row=4, column=1,padx=10,pady=10)
Button5 = Button(root, text="5", command=lambda: btnPress(5), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button5.grid(row=4, column=2,padx=10,pady=10)
Button6 = Button(root, text="6", command=lambda: btnPress(6), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button6.grid(row=4, column=3,padx=10,pady=10)
Button7 = Button(root, text="7", command=lambda: btnPress(7), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button7.grid(row=5, column=1,padx=10,pady=10)
Button8 = Button(root, text="8", command=lambda: btnPress(8), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button8.grid(row=5, column=2,padx=10,pady=10)
Button9 = Button(root, text="9", command=lambda: btnPress(9), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Button9.grid(row=5, column=3,padx=10,pady=10)
Plus = Button(root, text="+", command=lambda: btnPress("+"), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Plus.grid(row=3, column=4,padx=10,pady=10)
Minus = Button(root, text="-", command=lambda: btnPress("-"), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Minus.grid(row=4, column=4,padx=10,pady=10)
Multiply = Button(root, text="*", command=lambda: btnPress("*"), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Multiply.grid(row=5, column=4,padx=10,pady=10)
Divide = Button(root, text="/", command=lambda: btnPress("/"), borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Divide.grid(row=6, column=4,padx=10,pady=10)
Equal = Button(root, text="=", command=EqualPress, borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Equal.grid(row=6, column=3,padx=10,pady=10)
Clear = Button(root, text="C", command=ClearPress, borderwidth=2, relief=SOLID,font='arial 20 bold',width=3,height=1,bg='black',fg='white')
Clear.grid(row=6, column=1,padx=10,pady=10)

ANS = Button(root, text="ANSHUMAN",command=ailachu, borderwidth=2, relief=SOLID,font='arial 20 bold',width=18,height=1,bg='black',fg='white')
ANS.grid(row=7, column=1,padx=10,pady=10,columnspan=8)

root.mainloop()
