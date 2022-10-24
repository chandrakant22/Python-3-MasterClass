from tkinter import *

t = Tk()
t.geometry("300x100")
t.title("Asterisc")

def show_entry_fields():
    print("First Name: %s" % (e1.get()))
    str_var.set("Welcome %s" % (e1.get()))

def hiclick():
    str_var.set("Welcome Student!")
 

def byeclick():
    str_var.set("Bye Student!")
    

btn=Button(t,text="Hello",command = show_entry_fields)
btn.place(x=90,y=50)

btn=Button(t,text="Bye",command = byeclick)
btn.place(x=160,y=50)

e1=Entry(t)
e1.place(x=10,y=10)

str_var = StringVar()

str_var.set("")

l=Label(t,textvariable=str_var)
l.place(x=100,y=20)


t.mainloop()
