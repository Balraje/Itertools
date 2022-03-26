from tkinter import *
import sys
import mysql.connector

def save_data():
    conn = mysql.connector.connect()

root =Tk()
root.title('Employee Registration Form')
root.geometry('400x500')
f= Frame(root,)
f.pack()

fname = Label(f,text='First Name:')
lname = Label(f,text='Last Name:')

entry_fname = Entry(f,width=30)
entry_lname = Entry(f,width=30)

submit_button = Button(f, text= 'SAVE',width=20)
exit_button = Button(f,text ='EXIT',width=20)

fname.grid(row=0,column=0)
entry_fname.grid(row=0,column=1)

lname.grid(row=1,column=0)
entry_lname.grid(row=1,column=1)

submit_button.grid(row=2,column=0,command =save_data)
exit_button.grid(row=2,column=1)



root.mainloop()
