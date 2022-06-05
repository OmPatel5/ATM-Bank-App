import tkinter as tk
import csv
import pygame
import pandas as pd


def bank(userInfo):
    root2 = tk.Tk()
    root2.title("Bank")
    root2.geometry("1000x600")
        
    global amount 
    with open('test.csv', 'r') as test:
        for row in csv.DictReader(test):
            if row["Username"] == userInfo:
                amount = int(float(row["Amount"]))
    def dep_window():
        global amount
        def check_if_number():
            try:
                int(entryDeposit.get())  
                return 'Input is a Number.'
            except:
                error = tk.Toplevel()
                error.title("Error!")
                error_label = tk.Label(error, text = 'Error: User input is not a proper number or is blank.', font = ('Ink Free', 20))
                error_label.pack()
                error.mainloop()
        
        def add_amount():
            if check_if_number() == 'Input is a Number.':
                global amount
                if len(entryDeposit.get()) < 20 and len(str(amount)) < 20 and int(entryDeposit.get()) >= 0: 
                    amount += int(entryDeposit.get())
                    moneyLabel.config(text = "$ {}".format(amount))
                    deposit_window.destroy()   
                    with open('test.csv', 'r') as test:
                        i=0
                        for row in csv.DictReader(test):
                            i+=1
                            if row["Username"] == userInfo:
                                temp_num = i
                    df=pd.read_csv("test.csv")
                    df.loc[temp_num-1,'Amount'] = str(amount)
                    df.to_csv("test.csv",index=False)

                    
                else:
                    too_long = tk.Toplevel()
                    too_long.title("Error!")
                    too_long = tk.Label(too_long, text = 'Error: User input is too long or is negative.', font = ('Ink Free', 20))
                    too_long.pack()
                    too_long.mainloop()
        
        pygame.mixer.init()
        def play():
            pygame.mixer.music.load(r"C:\Users\omp16\Documents\TkinterProject\Cash-Register-Cha-Ching-Sound-Effect.wav")
            pygame.mixer.music.play(loops=0)

        deposit_window = tk.Toplevel()
        deposit_window.title("Deposit")
        deposit_window.geometry("800x400")

        deposit_label = tk.Label(deposit_window, text = 'Enter Amount for Depositing:', font = ('Ink Free', 40))
        deposit_label.pack()
        
        frameDepositWindow = tk.Frame(deposit_window, height = 100, width = 800)
        frameDepositWindow.pack()

        entryDeposit = tk.Entry(frameDepositWindow, font = ('Ink Free', 30), fg = "#00c3ff")
        entryDeposit.pack()
        
        frame_deposit_button = tk.Frame(deposit_window, height = 100, width = 300)
        frame_deposit_button.pack(pady = 20)

        deposit_button = tk.Button(frame_deposit_button, bg = "#9aeaed", text = 'Deposit!', font = ('Ink Free', 50), command=lambda:[check_if_number(), add_amount(), play()])
        deposit_button.pack()

    def wd_window():
        global amount
        def check_if_number():
            try:
                int(entryWidthdraw.get())  
                return 'Input is a Number.'
            except:
                error = tk.Toplevel()
                error.title("Error!")
                error_label = tk.Label(error, text = 'Error: User input is not a proper number or is blank.', font = ('Ink Free', 20))
                error_label.pack()
                error.mainloop()
        
        def sub_amount():
            if check_if_number() == 'Input is a Number.':
                global amount
                if len(entryWidthdraw.get()) < 20 and len(str(amount)) < 20 and int(entryWidthdraw.get()) >= 0 and int(entryWidthdraw.get()) <= amount: 
                    amount -= int(entryWidthdraw.get())
                    moneyLabel.config(text = "$ {}".format(amount))
                    withdraw_window.destroy()
                    with open('test.csv', 'r') as test:
                        i=0
                        for row in csv.DictReader(test):
                            i+=1
                            if row["Username"] == userInfo:
                                temp_num = i
                    df=pd.read_csv("test.csv")
                    df.loc[temp_num-1,'Amount'] = amount
                    df.to_csv("test.csv",index=False) 
                
                else:
                    too_long = tk.Toplevel()
                    too_long.title("Error!")
                    canvas = tk.Canvas(too_long, height = 100, width = 300)
                    canvas.pack()
                    too_long = tk.Label(canvas, text = "Error: User input is too long, is \nnegative, or you don't have that much\n money in your account.", font = ('Ink Free', 20))
                    too_long.pack()
                    too_long.mainloop()
        
        pygame.mixer.init()
        def play():
            pygame.mixer.music.load(r"C:\Users\omp16\Documents\Tkinter\Cash-Register-Cha-Ching-Sound-Effect.wav")
            pygame.mixer.music.play(loops=0)

        withdraw_window = tk.Toplevel()
        withdraw_window.title("Withdraw")
        withdraw_window.geometry("800x400")

        deposit_label = tk.Label(withdraw_window, text = 'Enter Amount for Withdrawing:', font = ('Ink Free', 40))
        deposit_label.pack()
        
        frameWithdrawtWindow = tk.Frame(withdraw_window, height = 100, width = 800)
        frameWithdrawtWindow.pack()

        entryWidthdraw = tk.Entry(frameWithdrawtWindow, font = ('Ink Free', 30), fg = "#00c3ff")
        entryWidthdraw.pack()
        
        frame_withdraw_button = tk.Frame(withdraw_window, height = 100, width = 300)
        frame_withdraw_button.pack(pady = 20)

        deposit_button = tk.Button(frame_withdraw_button, bg = "#ff756e", text = 'Withdraw!', font = ('Ink Free', 50), command=lambda:[check_if_number(), sub_amount(), play()])
        deposit_button.pack()
        


    frame = tk.Frame(root2, height = 100, width = 300, bg = "#00c3ff")
    frame.pack()

    bankLabel = tk.Label(frame, text = 'Hello ' + userInfo + "!", font = ('Ink Free', 100))
    bankLabel.pack()

    frameDEPOSIT = tk.Frame(root2)
    frameDEPOSIT.place(x = 100, rely = 0.6, height = 100, width = 300)

    buttonDEPOSIT = tk.Button(frameDEPOSIT, bg = "#ffa600", text = 'Deposit!', font = ('Ink Free', 50), height = 100, width = 300, activebackground = "#00c3ff", command = dep_window)
    buttonDEPOSIT.pack()

    frameWITHDRAW = tk.Frame(root2)
    frameWITHDRAW.place(x = 600, rely = 0.6, height = 100, width = 300)

    buttonWITHDRAW = tk.Button(frameWITHDRAW, bg = "#00c3ff", text = 'WithDraw!', font = ('Ink Free', 40), height = 100, width = 300, activebackground = "#ffa600", command = wd_window)
    buttonWITHDRAW.pack()

    moneyFrame = tk.Frame(root2)
    moneyFrame.place(x = 100, rely = 0.3, height = 100, width = 800)

        
    moneyLabel = tk.Label(moneyFrame, text = "$ {}".format(amount), font = ('Ink Free', 50))
    moneyLabel.pack()


    root2.mainloop()

