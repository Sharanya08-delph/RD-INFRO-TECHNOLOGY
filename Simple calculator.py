from tkinter import*

def button_click(num):
    global eq_text
    eq_text=eq_text+str(num)
    eq_label.set(eq_text)

def equal():
    global eq_text
    try:
        result=str(eval(eq_text))
        eq_label.set(result)
        eq_text=result
    except SyntaxError:
        eq_label.set("Error")
        eq_text=""
    except ZeroDivisionError:
        eq_label.set("Error")
        eq_text=""

def clear():
    global eq_text
    eq_label.set("")
    eq_text=""

def backspace():
    global eq_text
    eq_text=eq_text[:-1]
    eq_label.set(eq_text)
    
def animate_press(button):
    original = button["bg"]
    button.config(bg='#00008B')  
    button.after(100, lambda: button.config(bg=original))
    
calc=Tk()
calc.title("Simple Calculator")
calc.geometry("400x400")

eq_text=""
eq_label=StringVar()

label=Label(calc,textvariable=eq_label,font=('consolas',20),bg='beige',width=24,height=2)
label.pack()

frame=Frame(calc)
frame.pack()

b1=Button(frame,text=1,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b1),button_click(1)])
b1.grid(row=0,column=0)
b2=Button(frame,text=2,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b2),button_click(2)])
b2.grid(row=0,column=1)
b3=Button(frame,text=3,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b3),button_click(3)])
b3.grid(row=0,column=2)
b4=Button(frame,text=4,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b4),button_click(4)])
b4.grid(row=1,column=0)
b5=Button(frame,text=5,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b5),button_click(5)])
b5.grid(row=1,column=1)
b6=Button(frame,text=6,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b6),button_click(6)])
b6.grid(row=1,column=2)
b7=Button(frame,text=7,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b7),button_click(7)])
b7.grid(row=2,column=0)
b8=Button(frame,text=8,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b8),button_click(8)])
b8.grid(row=2,column=1)
b9=Button(frame,text=9,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b9),button_click(9)])
b9.grid(row=2,column=2)
b0=Button(frame,text=0,padx=7,pady=4,font=16,bg='#D8BFD8',fg='#000000',command=lambda:[animate_press(b0),button_click(0)])
b0.grid(row=3,column=0)
plus=Button(frame,text='+',padx=7,pady=4,font=16,bg='#FFD1DC',fg='#000000',command=lambda:[animate_press(plus),button_click('+')])
plus.grid(row=0,column=3)
minus=Button(frame,text='-',padx=7,pady=4,font=16,bg='#FFD1DC',fg='#000000',command=lambda:[animate_press(minus),button_click('-')])
minus.grid(row=1,column=3)
multiply=Button(frame,text='*',padx=7,pady=4,font=16,bg='#FFD1DC',fg='#000000',command=lambda:[animate_press(multiply),button_click('*')])
multiply.grid(row=2,column=3)
divide=Button(frame,text='/',padx=7,pady=4,font=16,bg='#FFD1DC',fg='#000000',command=lambda:[animate_press(divide),button_click('/')])
divide.grid(row=3,column=3)
equal=Button(frame,text='=',padx=7,pady=4,font=16,bg='#FFD1DC',fg='#000000',command=equal)
equal.grid(row=3,column=2)
decimal=Button(frame,text='.',padx=7,pady=4,font=16,bg='#FFD1DC',fg='#000000',command=lambda:[animate_press(decimal),button_click('.')])
decimal.grid(row=3,column=1)
backspace=Button(frame,text='X',padx=7,pady=4,font=16,bg='#FFD1DC',fg='#000000',command=backspace)
backspace.grid(row=4,column=1)

clear=Button(calc,text="clear",padx=20,pady=5,font=18,bg='#FFD1DC',fg='#000000',command=clear)
clear.pack()
calc.mainloop()














                   


