from tkinter import*
r=Tk()
r.title("button example")
''
r.geometry('1000x500')
l=Label(r,text="Registation Form",font=("bold",10),fg="red").pack()
l_1=Label(r,text="First Name")
l_1.place(x=80,y=130)
e=Entry(r).place(x=240,y=130)
l_2=Label(r,text="Last Name")
l_2.place(x=68,y=130)
e1=Entry(r).place(x=240,y=130)
la_3=Label(r,text="Email")
la_3.place(x=70,y=230)
e3=Entry(r)
e3.place(x=240,y=180)
r.mainloop()
