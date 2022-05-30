#bookreturn
from tkinter import *
import tkinter.messagebox
import database

def return_book(q):
    record_listed = database.list_records()
    count = False
    available = False
    if q.isnumeric() == False:
        tkinter.messagebox.showerror('Error','Must enter ID')
        #checks if value entered is numerical
        return
    if int(q) > 25 or int(q) < 0:
        tkinter.messagebox.showerror('Error','Incorrect Book ID')
        #limits book ID entered to ones that are possible
        pass
        
    for i in range (1,26):
        if record_listed["list" + str(i)][0] == int(q):
            if record_listed["list" + str(i)][5] >= 1000 and record_listed["list" + str(i)][5] <= 9999:
                #makes sure that the member ID in the record has a valid member ID
                #meaning that it is on loan
                count = True
                database.write_records(i,5,0)
                database.write_log(record_listed["list" + str(i)][2])
                #updates the records and the log files
            else:
                available = True
                
    if count == True and available == False:
        tkinter.messagebox.showinfo('Success','The Book has successfully been returned')
    elif available == True:
        tkinter.messagebox.showerror('Error','This book is already available')
