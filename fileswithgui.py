from filestesting import *
import csv
import tkinter as tk
from BankTkinter import *


def mainApp():
    root = tk.Tk()
    root.title("Log In")
    root.geometry('500x600')



    def check():
        ueinfo = username_entry.get()
        peinfo = password_entry.get()
        if (0 < len(ueinfo) < 17) and (0 < len(peinfo) < 17):
            return 'It is good!'
        else:
            error = tk.Toplevel()
            error_label = tk.Label(error, text = 'Username or Password needs to be \n more than 0 and less then 17 characters.', font = ('Ink Free', 20))
            error_label.pack()

    def check_file():
        ueinfo = username_entry.get()
        peinfo = password_entry.get()
        if check() == 'It is good!':
            if test(ueinfo, peinfo) == "Logged In Successfully!":
                print('logged in')
                return 'Logged In Successfully!'
            else:
                return 'Not Logged In Successfully!'

    def not_check_file():
        ueinfo = username_entry.get()
        if check() == 'It is good!':
            if check_file() == 'Not Logged In Successfully!':
                error = tk.Toplevel()
                error_label = tk.Label(error, text = 'Account not found. If \nnew, sign up!', font = ('Ink Free', 20))
                error_label.pack() 
            else:
                root.destroy()
                bank(ueinfo)
            
        
 

    def add_file():
        ueinfo = username_entry.get()
        peinfo = password_entry.get()
        if check() == 'It is good!': 
            if check_file() == 'Not Logged In Successfully!':
                add_acc(ueinfo, peinfo)
            else:
                error = tk.Toplevel()
                error_label = tk.Label(error, text = 'Account has already been \nmade or has just been \nmade.', font = ('Ink Free', 20))
                error_label.pack() 
        

        
        

    login = tk.Label(root, text = "Log In!", font=('Ink Free', 70), fg = "#ffb300")
    login.place(x=20)

    # username
    username_label = tk.Label(root, text='Enter Username', font=('Ink Free', 30), fg='#e85eeb')
    username_label.place(x=25, y=150)

    username_frame = tk.Frame(root)
    username_frame.place(x=30, y=200)

    username_entry = tk.Entry(username_frame, font = ('Ink Free', 20))
    username_entry.pack()

    #password
    password_label = tk.Label(root, text='Enter Password', font=('Ink Free', 30), fg='#00ddff')
    password_label.place(x=25, y=270)

    password_frame = tk.Frame(root)
    password_frame.place(x=30, y=320)

    password_entry = tk.Entry(password_frame, font = ('Ink Free', 20), show='*')
    password_entry.pack()


    #log in button
    login_button_frame = tk.Frame(root)
    login_button_frame.place(x=30, y=370)
    login_button = tk.Button(login_button_frame, text='Log In', font = ('Ink Free', 20), bg = '#00ddff', command = not_check_file)
    login_button.pack()

    #sign up button
    signup_button_frame = tk.Frame(root)
    signup_button_frame.place(x=150, y=370)

    signup_button = tk.Button(signup_button_frame, text='Sign Up', font = ('Ink Free', 20), bg = '#e85eeb', command = add_file)
    signup_button.pack()

    
    root.mainloop()

