import random

a= input('enter your name:')
b = input('website name for which you are using password:')
 

f = open('password manager.txt','a')
f.write(f'name:{a}  website name:{b}  password:{c}\n')
f.close()













from tkinter import *
import random, string
import pyperclip

root = Tk()
root.geometry("400x400")
root .resizable(0,0)
root.title("data flair -  password genrator")
Label(root, text = 'PASSWORD GENERATOR',font ='arial 15 bold ').pack()
Label(root, text ='DataFlair', font = 'arial 15 bold ').pack(side = BOTTOM)
pass_label = Label(root, text ='PASSSWORD LENGTH',font = 'arial 10 bold').pack()
pass_len =IntVar()
length = Spinbox(root, from_ = 8, to_ =32, textvariable = pass_len , width = 15).pack()
pass_str = StringVar()
def Generator():
    password = ''

    for x in range (0,8):
        Password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()- 8):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
    
Button(root, text = "GENERATE PASSWORD" , command = Generator ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
root.mainloop()

