from tkinter import *
import mysql.connector as mysql


def myinsert():

    db=mysql.connect(
    host="localhost",
    user="root",
    password="abc123",
    charset='utf8',
    database="mydb")

    cr=db.cursor()
    sql="INSERT INTO emp (id, name, address) VALUES (%s, %s, %s)"

    # id=eID.get()
    val = (eID.get(),eName.get(),eAddress.get())

    cr.execute(sql,val)

    db.commit()
    # print("db :",db)
    txt.set("Data Inserted! ")

    # print("your Data",eID.get(),eName.get(),eAddress.get())
    eID.set("")
    eName.set("")
    eAddress.set("")
    



t=Tk()

txt = StringVar()
eID= StringVar()
eName = StringVar()
eAddress = StringVar()

t.geometry("300x200")

i=Label(t,text="Id :").grid(row=0,column=0)
e=Entry(t,textvariable=eID).grid(row=0,column=1)

i1=Label(t,text="Name :").grid(row=1,column=0)
e1=Entry(t,textvariable=eName).grid(row=1,column=1)

i1=Label(t,text="Address :").grid(row=2,column=0)
e1=Entry(t,textvariable=eAddress).grid(row=2,column=1)

bInsert=Button(t, text = "insert",command=myinsert).grid(row = 3, column = 0) 


i3=Label(t,textvariable=txt).grid(row=3,column=1)

t.mainloop()
