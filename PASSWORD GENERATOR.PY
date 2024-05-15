import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import smtplib


gui = Tk()
gui.title('Password Generator')
gui.geometry('250x200')
gui.resizable(1,1)

def process():
    if(string_pass.get().isdigit() == False):
        messagebox.showerror("Error","Password length must be in numbers")
        return
    length = int(string_pass.get())

    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    all = lower + upper + num
    ran = random.sample(all,length)
    password = "".join(ran)
    messagebox.showinfo('Result', 'Password sent to your mail')
    Send_Mail(password)

def Send_Mail(Password):
    From_email = 'r22de118@gmail.com'
    From_password = 'yplp mtks cknb zjnj'
    To_email = 'lokeshck93@gmail.com'
    subject = 'PASSWORD'
    body = f'Hello,\n\n This is strong password {Password} \n\nBest regards\nPassword generator team,'
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(From_email, From_password)

    message = f'Subject: {subject}\n\n{body}'

    server.sendmail(From_email, To_email, message)

    server.quit()


string_pass = StringVar()
label = Label(text="Password Length").pack(pady=10)
txt = Entry(textvariable=string_pass).pack()
btn = Button(text="Generator", command=process).pack(pady=10)

gui.mainloop()