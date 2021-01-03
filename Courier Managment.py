from tkinter import *
import sqlite3
from tkinter import Menu
A=Tk()
A.title("Courier Management System")
A.geometry("560x300")
menu = Menu(A)
new_item = Menu(menu)
s=Menu(menu)
d=Menu(menu)
f=Menu(menu)
s.add_command(label="Undo")
s.add_command(label="Redo")
s.add_command(label="Cut")
s.add_command(label="copy")
s.add_command(label="Paste")
s.add_command(label="Select All")
s.add_command(label="Find")
new_item.add_command(label='New')
new_item.add_command(label='Open')
new_item.add_command(label='Recent Files')
new_item.add_command(label='Save')
new_item.add_command(label='Save As')
menu.add_cascade(label='File', menu=new_item)
menu.add_cascade(label='Edit', menu=s)
menu.add_cascade(label='Window',menu=d)
menu.add_cascade(label="Help",menu=f)
A.config(menu=menu)
def onclick1():
    B=Tk()
    B.title("LOGIN")
    B.geometry("300x200")
    menu = Menu(B)
    new_item = Menu(menu)
    s=Menu(menu)
    d=Menu(menu)
    f=Menu(menu)
    s.add_command(label="Undo")
    s.add_command(label="Redo")
    s.add_command(label="Cut")
    s.add_command(label="copy")
    s.add_command(label="Paste")
    s.add_command(label="Select All")
    s.add_command(label="Find")
    new_item.add_command(label='New')
    new_item.add_command(label='Open')
    new_item.add_command(label='Recent Files')
    new_item.add_command(label='Save')
    new_item.add_command(label='Save As')
    menu.add_cascade(label='File', menu=new_item)
    menu.add_cascade(label='Edit', menu=s)
    menu.add_cascade(label='Window',menu=d)
    menu.add_cascade(label="Help",menu=f)
    B.config(menu=menu)
    def login():
        e=Tk()
        e.title("LOGIN SUCCESSFULL")
        e.geometry("300x200")
        Label(e,text="LOGIN SUCCESSFULL",font="Times",fg="red").place(x=100,y=100)
    L1=Label(B,text="User Name")
    L1.place(x=50,y=30)
    L2=Label(B,text="Password")
    L2.place(x=50,y=90)
    txt1=Entry(B,width=20)
    txt1.place(x=120,y=30)
    txt2=Entry(B,width=20)
    txt2.place(x=120,y=90)
    btna=Button(B,text="LOGIN",bg="blue",fg="black",command=login,relief=GROOVE)
    btna.place(x=140,y=150)
    B.mainloop()
def onclick2():
    C=Tk()
    C.geometry("300x300")
    C.title("SIGN UP")
    menu = Menu(C)
    new_item = Menu(menu)
    s=Menu(menu)
    d=Menu(menu)
    f=Menu(menu)
    s.add_command(label="Undo")
    s.add_command(label="Redo")
    s.add_command(label="Cut")
    s.add_command(label="copy")
    s.add_command(label="Paste")
    s.add_command(label="Select All")
    s.add_command(label="Find")
    new_item.add_command(label='New')
    new_item.add_command(label='Open')
    new_item.add_command(label='Recent Files')
    new_item.add_command(label='Save')
    new_item.add_command(label='Save As')
    menu.add_cascade(label='File', menu=new_item)
    menu.add_cascade(label='Edit', menu=s)
    menu.add_cascade(label='Window',menu=d)
    menu.add_cascade(label="Help",menu=f)
    C.config(menu=menu)
    Firstname=StringVar()
    Email=StringVar()
    RegNo=StringVar()
    MobileNo=StringVar()
    def database():
     name=Firstname.get()
     email=Email.get()
     regno=RegNo.get()
     mobileno=MobileNo.get()
     conn=sqlite3.connect("kkc.db")
     #conn.execute("create table table1(Firstname varchar(50),Email text,RegNo varchar(10),MobileNo varchar(10))")
     conn.execute("insert into table1(Firstname,Email,RegNo,MobileNo) values(?,?,?,?)",(name,email,regno,mobileno))
     c=conn.execute("select * from table1")
     for i in c:
        print("name",i[0])
        print("email",i[1])
        print("Reg No",i[2])
        print("MobileNo",i[3])
     conn.commit()
    Label(C,text="Firstname").place(x=50,y=30)
    Entry(C,textvar=Firstname).place(x=120,y=30)
    Label(C,text="Email").place(x=50,y=60)
    Entry(C,textvar=Email).place(x=120,y=60)
    Label(C,text="Reg.No").place(x=50,y=90)
    Entry(C,textvar=RegNo).place(x=120,y=90)
    Label(C,text="Mobile No").place(x=50,y=120)
    Entry(C,textvar=MobileNo).place(x=120,y=120)
    selected = IntVar()
    rad1=Radiobutton(C,text="Male",value=1,variable=selected)
    rad1.place(x=80,y=150)
    rad2=Radiobutton(C,text="Female",value=2,variable=selected)
    rad2.place(x=180,y=150)
    Button(C,text="Submit",command=database,relief=GROOVE).place(x=150,y=190)
    C.mainloop()
def onclick3():
    D=Tk()
    D.title("TRACK CONSIGNMENT")
    D.geometry("400x200")
    menu = Menu(D)
    new_item = Menu(menu)
    s=Menu(menu)
    d=Menu(menu)
    f=Menu(menu)
    s.add_command(label="Undo")
    s.add_command(label="Redo")
    s.add_command(label="Cut")
    s.add_command(label="copy")
    s.add_command(label="Paste")
    s.add_command(label="Select All")
    s.add_command(label="Find")
    new_item.add_command(label='New')
    new_item.add_command(label='Open')
    new_item.add_command(label='Recent Files')
    new_item.add_command(label='Save')
    new_item.add_command(label='Save As')
    menu.add_cascade(label='File', menu=new_item)
    menu.add_cascade(label='Edit', menu=s)
    menu.add_cascade(label='Window',menu=d)
    menu.add_cascade(label="Help",menu=f)
    D.config(menu=menu)
    def data():
         a=sqlite3.connect('data.db')
         cursor=a.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY FROM Banks where ID=11710680")
         for row in cursor:
              print("ID=",row[0])
              print("NAME=",row[1])
              print("AGE",row[2])
              print("ADDRESS=",row[3])
              print("SALARY=",row[4],'\n')
         a.close()
    L6=Label(D,text="Consignment No.")
    L6.place(x=50,y=30)
    txt=Entry(D,width=20)
    txt.place(x=160,y=30)
    L9=Label(D,text="Mobile No.")
    L9.place(x=50,y=60)
    txtj=Entry(D,width=20)
    txtj.place(x=160,y=60)
    btn3=Button(D,text="TRACK",fg="black",bg="blue",command=data,relief=GROOVE)
    btn3.place(x=180,y=100)
    D.mainloop()
l=Label(A,text="\n\tWELCOME TO OUR COURIER MANAGMENT SYSTEM        ",fg="red",bg="white",font="Courier")
l.grid()
ls1=Label(A)
ls1.grid()
btn=Button(A,text="LOGIN",command=onclick1,fg="ghost white",font="Times",bg="slateblue",relief=GROOVE)
btn.grid(column=0,row=7)
btn1=Button(A,text="SIGN UP",command=onclick2,fg="ghost white",font="Times",bg="slateblue",relief=GROOVE)
ls2=Label(A)
ls2.grid()
btn1.grid(column=0,row=10)
btn2=Button(A,text="TRACK \nCONSIGNMENT",command=onclick3,fg="ghost white",bg="slateblue",font="Times",relief=GROOVE)
ls3=Label(A)
ls3.grid()
btn2.grid()
A.mainloop()
