##booksearch
from tkinter import *
import tkinter.messagebox
import database

def search(data):
    full_record = database.get_records()
    #gets the records as a string
    count = 0
    record_listed = database.list_records()
    #gets the record as a dict/list
    total = full_record['rec1']
    for i in range(1,26):
        if record_listed["list" + str(i)][2].lower() == data.lower():
            #Checks if the name match
            total = total + full_record["rec" + str(i+1)]
            #Adds the record to a string
            count +=1
    if count == 0:
        tkinter.messagebox.showerror('Not Found','No Book has that name')
    else:
        final = total.replace(':', '    ')
        #Better aesthetically
        print(final)

        #tkinter.messagebox.showinfo('Result',total)
        #Would be a message box but it formatted incorrectly


    

           
