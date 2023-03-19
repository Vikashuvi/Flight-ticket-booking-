import tkinter
from tkinter import messagebox
import mysql.connector
import tkinter as tk
from tkinter import ttk
root=tkinter.Tk()
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
root.configure(height=h,width=w,bg="#FFFFFF")
root.geometry("1300x700")
root.title("flight")
bg=tkinter.PhotoImage(file='air.png')
lbl=tkinter.Label(root,image=bg)
lbl.place(x=0,y=0)
root.iconbitmap(r'favicon.ico')


def insert():
    a=tb1.get()
    b=int(tb2.get())
    c=int(tb3.get())
    d=placechoosen.get()
    e=genderchoosen.get()
    f=destinationchoosen.get()
    con=mysql.connector.connect(host="localhost",user="root",password="vikash2005",database="plane")
    cur=con.cursor()
    cur.execute("insert into login values('%s','%s','%d','%s','%s','%s')"%(a,b,c,d,e,f))
    con.commit()
    messagebox.showinfo("PAYMENT SUCCESSFULL","your ticket has been booked!")

def clear():
    tb1.delete(0,"end")
    tb2.delete(0,"end")
    tb3.delete(0,"end")
    placechoosen.delete(0,"end")
    genderchoosen.delete(0,"end")
    destinationchoosen.delete(0,"end") 
    tb1.focus()

n = tk.StringVar()
placechoosen = ttk.Combobox(root,width = 25,font=("TimesNewRoman",20,"bold"),textvariable = n)
placechoosen['values'] = ('chennai',
						'delhi',
						'bangalore',
						'hyderabad',
						'kolkata',
						'mumbai')
placechoosen.place(x=290,y=380)
placechoosen.current()

n = tk.StringVar()
genderchoosen = ttk.Combobox(root,width = 25,font=("TimesNewRoman",20,"bold"),textvariable = n)
genderchoosen['values'] = ('male',
						'female')

genderchoosen.place(x=1000,y=235)
genderchoosen.current()

n = tk.StringVar()
destinationchoosen = ttk.Combobox(root,width = 25,font=("TimesNewRoman",20,"bold"),textvariable = n)
destinationchoosen['values'] = ('new york',
						'thailand',
                                                'singapore',
                                                'paris',
                                                'london',
                                                'sydney')

destinationchoosen.place(x=1000,y=380)
destinationchoosen.current()

    

lb1=tkinter.Label(root,text="TICKET BOOKING",font=("TimesNewRoman",25,"bold"),bd=10,bg="#FFFFFF",fg="#000000")
lb2=tkinter.Label(root,text="LUFTHANSA AIRLINES",font=("TimesNewRoman",30,"bold"),relief="raised",bd=10,bg="white",fg="dodgerblue")
lb1.place(x=40,y=100)
lb2.place(x=570,y=10)


lb2=tkinter.Label(root,text="NAME",font=("TimesNewRoman",20,"bold"),relief="flat",bd=10)
lb3=tkinter.Label(root,text="ORIGIN",font=("TimesNewRoman",20,"bold"),relief="flat",bd=10)
lb4=tkinter.Label(root,text="MEMBERS",font=("TimesNewRoman",20,"bold"),relief="flat",bd=10)
lb5=tkinter.Label(root,text="GENDER",font=("TimesNewRoman",20,"bold"),relief="flat",bd=10)
lb6=tkinter.Label(root,text="DESTINATION",font=("TimesNewRoman",20,"bold"),relief="flat",bd=10)
lb7=tkinter.Label(root,text="AMOUNT",font=("TimesNewRoman",20,"bold"),relief="flat",bd=10)

lb2.place(x=175,y=225)
lb3.place(x=130,y=375)
lb4.place(x=120,y=525)
lb5.place(x=800,y=225)
lb6.place(x=750,y=375)
lb7.place(x=800,y=525)



tb1=tkinter.Entry(root,font=("TimesNewRoman",25,"bold"))
tb2=tkinter.Entry(root,font=("TimesNewRoman",25,"bold"))
tb3=tkinter.Entry(root,font=("TimesNewRoman",25,"bold"))
tb1.place(x=325,y=235)
tb2.place(x=325,y=530)
tb3.place(x=1000,y=535)


but1=tkinter.Button(root,text="PAYMENT",font=("TimesNewRoman",20,"italic","bold"),relief="raised",bd=15,fg="snow",bg="lime",command=insert)
but2=tkinter.Button(root,text="CLEAR",font=("TimesNewRoman",20,"italic","bold"),relief="raised",bd=15,fg="snow",bg="red",command=clear)
but1.place(x=450,y=650)
but2.place(x=900,y=650)

root.mainloop()    
    

    
