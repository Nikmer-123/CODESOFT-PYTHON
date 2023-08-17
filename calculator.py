from tkinter import *
val=""
def btnClick(number):
    global val
    val=val+str(number)
    data.set(val)
def btnClear():
    global val
    val=""
    data.set("")


def btnEquals():
    global val
    result=""
    if val!="":
        try:
            result=str(eval(val))
        except:
            result="error"
            val=""
    data.set(result)


root=Tk()
root.title("My Calculator")
root.geometry("361x450+500+200")
data=StringVar()
display=Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel",20))
display.grid(row=0,columnspan=4)
btnSev=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(7))
btnSev.grid(row=1,column=0)
btneig=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(8))
btneig.grid(row=1,column=1)
btnnin=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(9))
btnnin.grid(row=1,column=2)
btnPlus=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,bg="green",command=lambda :btnClick('+'))
btnPlus.grid(row=1,column=3)
btnfour=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(4))
btnfour.grid(row=2,column=0)
btnfive=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(5))
btnfive.grid(row=2,column=1)
btnsix=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(6))
btnsix.grid(row=2,column=2)
btnMinus=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,bg="green",command=lambda :btnClick('-'))
btnMinus.grid(row=2,column=3)
btnone=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(1))
btnone.grid(row=3,column=0)
btntwo=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(2))
btntwo.grid(row=3,column=1)
btnthree=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(3))
btnthree.grid(row=3,column=2)
btnMul=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,bg="green",command=lambda :btnClick('*'))
btnMul.grid(row=3,column=3)
btnAllclr=Button(root,text="AC",font=("Ariel",12,"bold"),bd=12,height=2,width=6,bg="red",command=lambda :btnClear())
btnAllclr.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda :btnClick(0))
btn0.grid(row=4,column=1)
btndiv=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,bg="green",command=lambda :btnClick('/'))
btndiv.grid(row=4,column=2)
btnequlas=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,bg="green",command=lambda :btnEquals())
btnequlas.grid(row=4,column=3)
btndot=Button(root,text=".",font=("Ariel",12,"bold"),bd=12,height=2,width=10,command=lambda :btnClick('.'))
btndot.grid(row=5,column=1,columnspan=2)







root.mainloop()