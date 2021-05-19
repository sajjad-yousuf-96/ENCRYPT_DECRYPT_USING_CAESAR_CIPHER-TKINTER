import tkinter as tk
from tkinter import messagebox
import tkinter
from tkinter.constants import END
window1=tk.Tk()
window1.geometry("600x600")
window1.maxsize(600,600)
window1.minsize(600,600)
window1.title("CAESAR CIPHER TEXT")
window1.configure(bg='powderblue')
def encrypt():
    if e3.get() and e0.get():
        cipherlist=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        a=e0.get()
        c=e3.get()
        c=int(c)
        a=list(a)
        stri=""
        lst=[]
        for i in a:
            if i in cipherlist:
                num=cipherlist.index(i)
                num=num-c
                ans=cipherlist[num]
                lst.append(ans)
        e1.insert(0,stri.join(lst))
    else:
        messagebox.showwarning("CEASAR CIPHER","SOME FIELD MISSING")
def decrypt():
    if e3.get() and e0.get():
        cipherlist=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        a=e0.get()
        c=e3.get()
        a=list(a)
        c=int(c)
        stri=""
        lst=[]
        for i in a:
            ase=cipherlist.index(i)+c
            if i in cipherlist and ase < len(cipherlist):
                num=cipherlist.index(i)
                num=num+c
                ans=cipherlist[num]
                lst.append(ans)
            else:
                as1=cipherlist.index(i)
                if as1==23:
                    num=c-((len(cipherlist)-1)-as1)-1
                    ans=cipherlist[num]
                    lst.append(ans)
                elif as1==24:
                    num=c-((len(cipherlist)-1)-as1)-1
                    ans=cipherlist[num]
                    lst.append(ans)
                else:
                    num=c-((len(cipherlist)-1)-as1)-1
                    ans=cipherlist[num]
                    lst.append(ans)
        e2.insert(0,stri.join(lst))
    else:
        messagebox.showwarning("CEASAR CIPHER","SOME FIELD MISSING")
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e0.delete(0,END)
tt=tk.StringVar()
yt=tk.StringVar()
anst=tk.StringVar()
num1=tk.StringVar()
Label0=tk.Label(window1,text='TEXT',fg='BLACK',bg='powderblue',font=('Times New Roman',18))
Label0.place(x=70,y=104)
Label1=tk.Label(window1,text='CIPHER TEXT',fg='BLACK',bg='powderblue',font=('Times New Roman',18))
Label1.pack()
Label2=tk.Label(window1,text='ENCRYPT TEXT',fg='BLACK',bg='powderblue',font=('Times New Roman',18))
Label2.place(x=70,y=144)
Label3=tk.Label(window1,text='YOUR SHIFT',fg='BLACK',bg='powderblue',font=('Times New Roman',18))
Label3.place(x=70,y=204)
Label2=tk.Label(window1,text='DECRYPT TEXT',fg='BLACK',bg='powderblue',font=('Times New Roman',18))
Label2.place(x=70,y=174)
e0=tk.Entry(window1,textvariable='tt',width=35,font=('Times New Roman',11))
e0.place(x=250,y=110)
e1=tk.Entry(window1,textvariable='yt',width=35,font=('Times New Roman',11))
e1.place(x=250,y=150)
e3=tk.Entry(window1,textvariable='num',width=35,font=('Times New Roman',11))
e3.place(x=250,y=210)
e2=tk.Entry(window1,textvariable='anst',width=35,font=('Times New Roman',11))
e2.place(x=250,y=180)
b1=tk.Button(window1,text='DECRYPT WITH CEASAR CIPHER',width=35,fg='BLACK',font=('Times New Roman',11),command=decrypt)
b1.place(x=170,y=350)
b2=tk.Button(window1,text='ENCRYPT WITH CEASAR CIPHER',width=35,fg='BLACK',font=('Times New Roman',11),command=encrypt)
b2.place(x=170,y=300)
b3=tk.Button(window1,text='CLEAR',width=35,fg='BLACK',font=('Times New Roman',11),command=clear)
b3.place(x=170,y=400)
window1.mainloop()