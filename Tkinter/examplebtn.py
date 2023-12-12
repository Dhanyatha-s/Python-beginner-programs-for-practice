from  tkinter import*
r=Tk()
r.title("button example")
''
r.geometry('300x200')
''
b=Button(r,text='Apply', width=25,bg='red',command=r.destroy)
b.pack()
r.mainloop()


