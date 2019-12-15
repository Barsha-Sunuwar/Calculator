from tkinter import*
def enter(a):
  global operator
  operator = operator + str(a)
  number.set(operator)
def opbut():
  global operator
  add =str(eval(operator))
  operator= ''
  number.set(add)
def opbut():
  global operator
  subtract= str(eval(operator))
  operator= ''
  number.set(subtract)

def opbut():
  global operator
  divide= str(eval(operator))
  operator= ''
  number.set(divide)

def opbut():
  global operator
  multiply= str(eval(operator))
  operator = ''
  number.set(multiply)

def clrbut():
  global operator
  operator=""
  number.set('')
#for menubar that appears on top when calculator is opened#
root=Tk()
root.title("Calculator")
menubar= Menu(root)
#----for View Menu----#
view= Menu(menubar)
view.add_command(label="Standard", command=" ")
view.add_command(label="Scientific", command=" ")
view.add_separator()
view.add_command(label="Basic", command=" ")
view.add_command(label="Currency converter", command=" ")
view.add_command(label="Date calculation", command=" ")
view.add_separator()
view.add_command(label="Exit", command=root.quit)
#----Add sub-menu to the main menu(must use otherwise the lebel will not appear)----#
menubar.add_cascade(label="View", menu=view)
#----for Edit Menu----#
editmenu=Menu(menubar)
editmenu.add_command(label="Undo", command=" ")
editmenu.add_command(label="Cut", command=" ")
editmenu.add_command(label="Copy", command=" ")
editmenu.add_command(label="Paste", command=" ")
menubar.add_cascade(label="Edit", menu=editmenu)
#----for Help Menu----#
helpmenu=Menu(menubar)
helpmenu.add_command(label="About calculator", command=" ")
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)

#----For Calculator part----#
root.geometry('470x450')
root.resizable(0, 0)
root.config(background="orange")
number =StringVar ()
operator= " "
expression_field = Entry(root, textvariable=number, font=('', 30))
expression_field.grid(columnspan=5, padx=10, pady=30)
number.set('Enter numbers')

#----For making Buttons----#
but1=Button(root, text='1', font=(" ", 25), bg="sky blue", fg="black", command=lambda: enter(1), height=1, width=4)
but1.grid(row=2, column=0, pady=2)
but2=Button(root, text='2', font=(" ", 25), bg="skyblue", fg="black", command=lambda: enter(2), height=1, width=4)
but2.grid(row=2, column=1, pady=2)
but3=Button(root, text='3', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter(3), height=1, width=4)
but3.grid(row=2, column=2, pady=2)
but4=Button(root, text='4', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter(4), height=1, width=4)
but4.grid(row=3, column=0, pady=2)
but5=Button(root, text='5', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter(5), height=1, width=4)
but5.grid(row=3, column=1, pady=2)
but6=Button(root, text='6', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter(6), height=1, width=4)
but6.grid(row=3, column=2, pady=2)
but7=Button(root, text='7', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter(7), height=1, width=4)
but7.grid(row=4, column=0, pady=2)
but8=Button(root, text='8', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter(8), height=1, width=4)
but8.grid(row=4, column=1, pady=2)
but9=Button(root, text='9', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter(9), height=1, width=4)
but9.grid(row=4, column=2, pady=2)
but0=Button(root, text='0', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter(0), height=1, width=9)
but0.grid(row=5, column=1, columnspan=2, pady=2,padx=2)
butadd=Button(root, text='+', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter('+'), height=1, width=4)
butadd.grid(row=5, column=3, pady=2)
butsubtract=Button(root, text='-', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter('-'), height=1, width=4)
butsubtract.grid(row=4, column=3, pady=2)
butdivide=Button(root, text='/', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter('/'), height=1, width=4)
butdivide.grid(row=2, column=3, pady=2)
butmultiply=Button(root, text='*', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter('*'), height=1, width=4)
butmultiply.grid(row=3, column=3, pady=2)
butdec=Button(root, text='.', font=(" ", 25), bg="sky blue", fg="black", command=lambda:enter('.'), height=1, width=4)
butdec.grid(row=5, column=0, pady=2)
butequal=Button(root, text='=', font=("", 25), bg="sky blue", fg="black", command=opbut, height=3, width=4)
butequal.grid(row=4, column=4, rowspan=2, pady=2)
butclear=Button(root, text='Clear', font=("", 25), bg="sky blue", fg="black", command=clrbut, height=3, width=4)
butclear.grid(row=2, column=4,rowspan=2, pady=2)

root.mainloop()

