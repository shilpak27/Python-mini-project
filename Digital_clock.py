import tkinter as tk
from time import strftime  # time- time related function
# strftime we can forword time as per our requirment
root = tk.Tk()  # main window where we can show main component
root.title("Digital Clock")


def time():  # function that can update time and date and display on lable
    string = strftime('%H:%M:%S %p \n %D')
    # from the config method of lable object we will assign the string function
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=('calibri', 50, 'bold '),
                 background='yellow', foreground='black')
label.pack(anchor='center')

time()

root.mainloop()  # mainloop is the method in the tkinter module which keep window in loop
