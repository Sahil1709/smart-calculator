from tkinter import *
from functools import partial

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def result(text,res):
    commands = {
        'add':add,'+':add,'addition':add,'plus':add,'sum':add,
        'minus':sub,'sub':sub,'subtract':sub,'subtraction':sub,'-':sub,'ghatav':sub,
        'mul':mul,'multiply':mul,'*':mul,'x':mul,'guna':mul,'multiplication':mul,
        'div':div,'division':div,'divide':div,'/':div,
        'mod':mod,'modu':mod,'modulus':mod,'%':mod
    }
    text = text.get().lower()
    list1 = text.split()
    list2 = []
    print(list1)
    for i in list1:
        try:
            list2.append(float(i))
            print(list2)
        except ValueError:
            pass

    for i in list1:
        if i in commands.keys():
            r = commands[i](list2[0],list2[1])
            res.set(r)
            l4.config(text='Theres your answer')
            break
    else:
        l4.config(text='Command not found')
    


win = Tk()
win.title('Smarty')
win.config(bg='light yellow')
win.geometry('500x400')

text = StringVar()
res = StringVar()

l1 = Label(win,text='Smart Calculator',font='Courier 24')
l2 = Label(win,text='You can type english sentences and can get the result below',font=18)
l3 = Label(win,text='What can i help u with ?',font=18)
e1 = Entry(win,textvariable=text)
result = partial(result,text,res)
b1 = Button(win,text='Just this',font=18,command=result)
e2 = Entry(win,textvariable=res)
l4 = Label(win,text='Errors will be displayed here',font=18)

l1.pack(pady=10)
l2.pack(pady=10)
l3.pack(pady=10)
e1.pack(pady=10)
b1.pack(pady=10)
e2.pack(pady=10)
l4.pack(pady=10)

win.mainloop()