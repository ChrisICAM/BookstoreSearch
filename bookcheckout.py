#bookcheckout
from tkinter import *
import tkinter.messagebox
import database

def checkout_book(b_id, m_id):
    record_listed = database.list_records()
    #gets all the records in the db with each id as a seperate list
    available = False
    for i in range (1,26):
        if record_listed["list" + str(i)][0] == int(b_id):
            #checks Book ID to all the ID in the db
            if record_listed["list" + str(i)][5] == 0:
                #checks if the member ID is 0 meaning its available
                available = True
                database.write_records(i,5,m_id)
                #writes to the db the updated change
                break

            else:
                pass
                
    if available:
        tkinter.messagebox.showinfo('Success','The Book has successfully been check-out')
    else:
        tkinter.messagebox.showerror('Error','This Book is not available')
