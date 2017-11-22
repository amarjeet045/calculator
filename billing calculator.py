from Tkinter import *
root=Tk()
root.title('Amarjeet')
Label(root,text="Select Your Breakfast",font="times 15 bold",bg="red").grid(columnspan=10)
Label(root,text="(Breakfast Calculator)",font="times 15 bold underline",bg="yellow").grid(columnspan=10)
v2=IntVar()
v3=IntVar()
v4=IntVar()
v5=IntVar()
v6=IntVar()
v7=IntVar()
v8=IntVar()
v9=IntVar()
v10=IntVar()
v11=IntVar()
v12=IntVar()
v13=IntVar()
v14=IntVar()
v15=IntVar()
v16=IntVar()
v17=IntVar()

def calc():
    sumi=v2.get()+v3.get()+v4.get()+v5.get()+v6.get()+v7.get()+v8.get()+v9.get()+v10.get()+v11.get()+v12.get()+v13.get()+v14.get()+v15.get()+v16.get()+v17.get()
    Label(root,text=("Total amount = Rs." +str(sumi)),font="veranda 10 bold").grid(row=11,column=0)

def close():
    root.destroy()

Checkbutton(root,text="Macroni(105)",variable=v2,onvalue=105,font="arial 10 bold").grid(row=2,column=0,sticky=W)
Checkbutton(root,text="Pav bhaji(110)",variable=v3,onvalue=110,font="arial 10 bold").grid(row=3,column=0,sticky=W)
Checkbutton(root,text="Sandwich(80)",variable=v4,onvalue=80,font="arial 10 bold").grid(row=4,column=0,sticky=W)
Checkbutton(root,text="Pasta(80)",variable=v5,onvalue=80,font="arial 10 bold").grid(row=5,column=0,sticky=W)
Checkbutton(root,text="   Aloo Paratha(200)",variable=v6,onvalue=200,font="arial 10 bold").grid(row=6,column=0,sticky=W)
Checkbutton(root,text="omelete(30)",variable=v7,onvalue=30,font="arial 10 bold").grid(row=7,column=0,sticky=W)
Checkbutton(root,text="   poha(50)",variable=v8,onvalue=50,font="arial 10 bold").grid(row=8,column=0,sticky=W)
Checkbutton(root,text="fruits(40)",variable=v9,onvalue=40,font="arial 10 bold").grid(row=2,column=1,sticky=W)
Checkbutton(root,text="noodles(120)",variable=v10,onvalue=120,font="arial 10 bold").grid(row=3,column=1,sticky=W)
Checkbutton(root,text="bread butter(20)",variable=v11,onvalue=20,font="arial 10 bold").grid(row=4,column=1,sticky=W)
Checkbutton(root,text="egg(20)",variable=v12,onvalue=20,font="arial 10 bold").grid(row=5,column=1,sticky=W)
Checkbutton(root,text="sprouts(65)",variable=v13,onvalue=65,font="arial 10 bold").grid(row=6,column=1,sticky=W)
Checkbutton(root,text="idli(60)",variable=v14,onvalue=60,font="arial 10 bold").grid(row=7,column=1,sticky=W)
Checkbutton(root,text="porage(55)",variable=v15,onvalue=55,font="arial 10 bold").grid(row=8,column=1,sticky=W)
Checkbutton(root,text="upama(20)",variable=v16,onvalue=20,font="arial 10 bold").grid(row=9,column=0,sticky=W)
Checkbutton(root,text="milk  corn flakes(25)",variable=v17,onvalue=25,font="arial 10 bold").grid(row=9,column=1,sticky=W)




Button(root,text="Check Ruppes",command=calc).grid(row=10,column=0)
Button(root,text="Exit",command=close).grid(row=10,column=1)
root.geometry("400x500+100+150")













root.mainloop()
