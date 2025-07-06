from tkinter import*
from random import randint

def random():
    password_entry.delete(0,END)
    password_length=int(entry.get())
    new_password=""

    for x in range(password_length):
        new_password+=chr(randint(33,126))

    password_entry.insert(0,new_password)

def copy_to_clipboard():
    pwd.clipboard_clear()
    pwd.clipboard_append(password_entry.get())

def animate_press(button):
    original=button["bg"]
    button.config(bg="pink")
    button.after(100,lambda:button.config(bg=original))

pwd=Tk()
pwd.title("Password generator")
pwd.geometry("500x300")
new_password=chr(randint(33,126))
label=LabelFrame(pwd,text="Length of the password",padx=10,pady=20,font=("consolas",16),bg="beige")
label.pack()

entry=Entry(label)
entry.pack()

password_entry=Entry(pwd,text="",font=("Arial",20))
password_entry.pack(pady=20)

frame=Frame(pwd)
frame.pack()

b1= Button(frame,text="Generate password",bg="#AEC6CF",pady=10)
b1.config(command=lambda:[animate_press(b1),random()])
b1.grid(row=0,column=0)
b2= Button(frame,text="copy ",bg="#AEC6CF",pady=10)
b2.config(command=lambda:[animate_press(b2),copy_to_clipboard()])
b2.grid(row=2,column=0)

pwd.mainloop()


              
