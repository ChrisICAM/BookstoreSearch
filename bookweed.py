#bookweed
from tkinter import *
import tkinter.messagebox
import database
import booksearch
import matplotlib.pyplot as plt

global names
global num
names = []
num = []

def book_weeding(choice):
    logs = database.list_logs()
    for i in range(1,len(logs)+1):
        names.append(logs["log"+str(i)][0])
        num.append(logs["log"+str(i)][1])
        #calls the dict and appends each item to a different list
    if choice:
        full_report()
    else:
        quick_report()

def quick_report():
    a = sorted(zip(num, names))[:3]
    #creates a tuple with the items sorts it in asc. order
    #then takes the first 3 elements (3 lowest return logs)
    text = 'These book titles are least popular and should be weeded:\n'
    text1 = '      ' + a[0][1] + '\n      ' + a[1][1] + '\n      ' + a[2][1]
    tkinter.messagebox.showinfo('Quick Weeding Report', text+text1)
    #shows a message box of the 3 lowest return logs
    #means they are the least popular
    del num[:]
    del names[:]
    #resets the global variables
    

def full_report():
    plt.bar(names, num)
    plt.show()
    #exports a full graph so you can see the logs in a bar chart form


