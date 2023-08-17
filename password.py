from tkinter import *
import string
import random
import pyperclip
def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_char=string.punctuation
    all=small_alphabets+capital_alphabets+numbers+special_char
    pass_length=(int)(length_box.get())
    if choice.get()==1:
        passField.insert(0,random.sample(small_alphabets,pass_length))
    if choice.get()==2:
        passField.insert(0,random.sample(small_alphabets+capital_alphabets,pass_length))
    if choice.get()==3:
        passField.insert(0,random.sample(all,pass_length))
def copyBtn():
    result=passField.get()
    pyperclip.copy(result)

root=Tk()
root.geometry('790x570+500+200')
root.config(bg="gray")
choice=IntVar()
Font=('arial',13,'bold')
root.title("Password Generator")
nameLabel=Label(root,text="Enter your name :",font=('times new roman',20,'bold'),bg='black',fg='white')
nameLabel.place(relx=0.2,rely=0.1,anchor=CENTER)
Field1=Entry(root,width=25,bd=2,font=Font,bg='blue',fg='white')
Field1.place(relx=0.6,rely=0.1,anchor=CENTER)

comLabel=Label(root,text="Enter complexity Level:",font=('times new roman',20,'bold'),bg='black',fg='white')
comLabel.place(relx=0.2,rely=0.3,anchor=CENTER)

weakradioButton=Radiobutton(root,text="Weak",value=1,variable=choice,font=Font,bg='red')
weakradioButton.place(relx=0.5,rely=0.3,anchor=CENTER)

mediumradioButton=Radiobutton(root,text="Medium",value=2,variable=choice,font=Font,bg='yellow')
mediumradioButton.place(relx=0.7,rely=0.3,anchor=CENTER)
strongradioButton=Radiobutton(root,text="Strong",value=3,variable=choice,font=Font,bg='green')
strongradioButton.place(relx=0.9,rely=0.3,anchor=CENTER)
lengthLabel=Label(root,text="Enter Password Length :",font=('times new roman',20,'bold'),bg='black',fg='white')
lengthLabel.place(relx=0.2,rely=0.5,anchor=CENTER)
length_box=Spinbox(root,from_=5,to_=18,width=5,font=Font,bg='blue',fg='white')
length_box.place(relx=0.6,rely=0.5,anchor=CENTER)
geneButton=Button(root,text="Generate Password :",font=Font,bg='black',fg='white',command=lambda:generator())
geneButton.place(relx=0.2,rely=0.7,anchor=CENTER)
passField=Entry(root,width=25,bd=2,font=Font,bg='blue',fg='white')
passField.place(relx=0.6,rely=0.7,anchor=CENTER)
copyButton=Button(root,text="Copy",font=Font,command=lambda: copyBtn())
copyButton.place(relx=0.5,rely=0.9,anchor=CENTER)



root.mainloop()