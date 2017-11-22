from Tkinter import*
root=Tk()
root.title("Calculator Python")
Label(root,text="enter a number").grid(column=0,row=0,columnspan=4)
e=Entry(root,width=16,bd=5,justify="right")
e.grid(column=0,columnspan=4,row=0)
def insert(x):
    
    e.insert(END,x)
def clear():
    e.delete(0,END)
def result(x):
    y=eval(e.get())
    clear()
    e.insert(END,y)
def clearr():
    value=e.get()
    value=value[:-1]
    e.delete(0,END)
    e.insert(0,value)
    
Button(root,text="9",bd=5,command=lambda:insert(9)).grid(column=0,row=1)
Button(root,text="8",bd=5,command=lambda:insert(8)).grid(column=1,row=1)
Button(root,text="7",bd=5,command=lambda:insert(7)).grid(column=2,row=1)
Button(root,text="C",bd=5,command=lambda:clear()).grid(column=3,row=1)
Button(root,text="6",bd=5,command=lambda:insert(6)).grid(column=0,row=2)
Button(root,text="5",bd=5,command=lambda:insert(5)).grid(column=1,row=2)
Button(root,text="4",bd=5,command=lambda:insert(4)).grid(column=2,row=2)
Button(root,text="+",bd=5,command=lambda:insert('+')).grid(column=3,row=2)
Button(root,text="3",bd=5,command=lambda:insert(3)).grid(column=0,row=3)
Button(root,text="2",bd=5,command=lambda:insert(2)).grid(column=1,row=3)
Button(root,text="1",bd=5,command=lambda:insert(1)).grid(column=2,row=3)
Button(root,text="-",bd=5,command=lambda:insert('-')).grid(column=3,row=3)
Button(root,text="0",bd=5,command=lambda:insert(0)).grid(column=0,row=4)
Button(root,text=".",bd=5,command=lambda:insert('.')).grid(column=1,row=4)
Button(root,text="=",bd=5,command=lambda:result('=')).grid(column=2,row=4)
Button(root,text="/",bd=5,command=lambda:insert('/')).grid(column=3,row=4)
Button(root,text="CC",bd=5,command=lambda:clearr()).grid(column=0,row=5)
Button(root,text="*",bd=5,command=lambda:insert('*')).grid(column=1,row=5)

root.mainloop()

