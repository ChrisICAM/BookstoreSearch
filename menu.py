#menu
from tkinter import *
import tkinter.messagebox
import matplotlib.pyplot as plt 
import bookcheckout  #this allows me to import the functions from 
import bookreturn   # within the other python files so this is the main
import booksearch  # file that will do everything at once, the main hub
import bookweed
import database

def change_frame(frame,new):
        frame.pack_forget()
        new.pack()
        
#This is the function use to swap frames as it forgets the first frame
#then the second frame is packed in the same place as the first frame
        
def close(root):
    answer = tkinter.messagebox.askquestion('Closing', 'Are you sure you want to close the program?')
    #Popup box confirming if you want to close the program        
    if answer == 'yes':
        root.destroy()

    elif answer == 'no':
        pass

def searching(event):
        data = search_bar.get()
        #gets the data within the entry field
        booksearch.search(data)

def returning(event):
        data = r_bar.get()
        bookreturn.return_book(data)

def weeding(switch):
        #switch is an arg that will differentiate between a quick or full report
        bookweed.book_weeding(switch)

def checkout(event):
        data = c_bar.get()
        data1 = c1_bar.get()
        if data == '' or data1 == '':
                tkinter.messagebox.showerror('Error', 'Both entries need to be entered')
                #checks if the entry boxes are empty
        elif data.isnumeric() == False or data1.isnumeric() == False:
                tkinter.messagebox.showerror('Error', 'Both entries have to be numbers')
        elif int(data) > 25 or int(data) < 0:
                tkinter.messagebox.showerror('Error', 'Insufficient Book ID')
                #makes sure that the Book ID entered is valid
        elif int(data1) < 1000 or int(data1) > 9999:
                tkinter.messagebox.showerror('Error', 'Insufficient Member ID')
                #makes sure that the Member ID entered is valid
        else:
                bookcheckout.checkout_book(data,data1)

##############################################################
#########-------------------MAIN----------------------########
##############################################################

root = Tk() 
root.title('Library Menu') 
root.resizable(0,0)
#make it so that the window cannot be resized
root.wm_attributes('-topmost',1)
# Window is placed to the front of all things windows on screen at all times
f1 = Frame(root)
search_frame = Frame(root)
checkout_frame = Frame(root)
return_frame = Frame(root)
weed_frame = Frame(root)
f1.pack()

# This adds frames to the window so they are easily swappable with each other


canvas = Canvas(f1, width = 500, height = 500, bd = 1,
                highlightthickness = 1, bg = 'alice blue')
canvas.pack() 

canvas.create_text(250,35,text = "Welcome",font = ('Times',36))

canvas.create_line(165,55,345,55)
canvas.create_line(185,67,325,67)


button1 = Button(f1, text = 'Search',font = ('Helvetica',18),
                 fg = 'light cyan', bg = 'light goldenrod',
                 command=lambda : change_frame(f1,search_frame)) #these buttons swap the pages
button1.pack()
button1_window = canvas.create_window(150, 200, width = 180, height = 100, window=button1)
#I have to make a button window as you can't put a button striaght on the canvas
#So a separate window is made to place on top of the canvas with just the button

button2 = Button(f1, text = 'Return',font = ('Helvetica',18),
                 fg = 'light cyan', bg = 'coral2',
                 command=lambda : change_frame(f1,return_frame))
button2.pack()
button2_window = canvas.create_window(150, 330, width = 180, height = 100, window=button2)

button3 = Button(f1, text = 'CheckOut',font = ('Helvetica',18),
                 fg = 'light cyan', bg = 'PaleVioletRed2',
                 command=lambda : change_frame(f1,checkout_frame))
button3.pack()
button3_window = canvas.create_window(360, 200, width = 180, height = 100, window=button3)

button4 = Button(f1, text = 'Weed',font = ('Helvetica',18),
                 fg = 'light cyan', bg = 'SeaGreen2',
                 command=lambda : change_frame(f1,weed_frame))
button4.pack()
button4_window = canvas.create_window(360, 330, width = 180, height = 100, window=button4)

button5 = Button(f1, text = 'Quit',font = ('Helvetica',15),
                bg = 'Red2', command=lambda root=root:close(root))
button5.pack()
button5_window = canvas.create_window(460, 480, width = 60, height = 35, window=button5)

#Created a button for each main function of the program

##########################
###### Search Page #######
##########################

s_canvas = Canvas(search_frame, width = 500, height = 500, bd = 1,
                highlightthickness = 1, bg = 'alice blue')
s_canvas.pack()

s_canvas.create_text(250,35,text = "Search",font = ('Times',36))

s_canvas.create_line(185,55,315,55)
s_canvas.create_line(205,67,295,67)

s_canvas.create_text(250,155,text = "Book Name:",font = ('Times',28))
s_canvas.create_text(250,235,text = "Press Enter to get the results",font = ('Times',20))

search_bar = Entry(search_frame,font = ('Helvetica',20))
search_bar.place(width=200,height=40)
search_bar.pack()
search_bar_window = s_canvas.create_window(250,200, window=search_bar)
search_bar.bind('<Return>', searching)
#assigns the enter key to a function when typing in the entry box

return_button = Button(search_frame, text = 'Return',font = ('Helvetica',17),
                bg = 'Red2', command=lambda : change_frame(search_frame, f1))
return_button.pack()
return_button_window = s_canvas.create_window(60, 430, width = 90, height = 55, window=return_button)
#This is a return button to go to the previous page

q_button = Button(search_frame, text = 'Quit',font = ('Helvetica',15),
                bg = 'Red2', command=lambda root=root:close(root)) #forces the program to close
q_button.pack()
q_button_window = s_canvas.create_window(460, 480, width = 60, height = 35, window=q_button)

##########################
##### Check-Out Page #####
##########################

c_canvas = Canvas(checkout_frame, width = 500, height = 500, bd = 1,
                highlightthickness = 1, bg = 'alice blue')
c_canvas.pack()

c_canvas.create_text(250,35,text = "Check-Out",font = ('Times',36))

c_canvas.create_line(150,55,355,55)
c_canvas.create_line(180,67,323,67)

c_bar = Entry(checkout_frame,font = ('Helvetica',20))
c_bar.place(width=200,height=40)
c_bar.pack()
c_bar_window = c_canvas.create_window(250,200, window=c_bar)

c1_bar = Entry(checkout_frame,font = ('Helvetica',20))
c1_bar.place(width=200,height=40)
c1_bar.pack()
c1_bar_window = c_canvas.create_window(250,280, window=c1_bar)

c_canvas.create_text(250,155,text = "Book ID:",font = ('Times',28))
c_canvas.create_text(250,245,text = "Member ID:",font = ('Times',28))
c_canvas.create_text(250,325,text = "Press Enter to Check-Out a Book",font = ('Times',19))

c_bar.bind('<Return>', checkout)
c1_bar.bind('<Return>', checkout)

return_button = Button(checkout_frame, text = 'Return',font = ('Helvetica',17),
                bg = 'Red2', command=lambda : change_frame(checkout_frame, f1))
return_button.pack()
return_button_window = c_canvas.create_window(60, 430, width = 90, height = 55, window=return_button)

q_button = Button(checkout_frame, text = 'Quit',font = ('Helvetica',15),
                bg = 'Red2', command=lambda root=root:close(root))
q_button.pack()
q_button_window = c_canvas.create_window(460, 480, width = 60, height = 35, window=q_button)

##########################
###### Return Page #######
##########################

r_canvas = Canvas(return_frame, width = 500, height = 500, bd = 1,
                highlightthickness = 1, bg = 'alice blue')
r_canvas.pack()

r_canvas.create_text(250,35,text = "Return Book",font = ('Times',36))

r_canvas.create_line(130,55,370,55)
r_canvas.create_line(155,67,335,67)

r_canvas.create_text(250,155,text = "Book ID:",font = ('Times',28))
r_canvas.create_text(250,235,text = "Press Enter to return book",font = ('Times',20))

r_bar = Entry(return_frame,font = ('Helvetica',20))
r_bar.place(width=200,height=40)
r_bar.pack()
r_bar_window = r_canvas.create_window(250,200, window=r_bar)
r_bar.bind('<Return>', returning)

return_button = Button(return_frame, text = 'Return',font = ('Helvetica',17),
                bg = 'Red2', command=lambda : change_frame(return_frame, f1))
return_button.pack()
return_button_window = r_canvas.create_window(60, 430, width = 90, height = 55, window=return_button)

q_button = Button(return_frame, text = 'Quit',font = ('Helvetica',15),
                bg = 'Red2', command=lambda root=root:close(root))
q_button.pack()
q_button_window = r_canvas.create_window(460, 480, width = 60, height = 35, window=q_button)

##########################
###### Weeding Page ######
##########################

w_canvas = Canvas(weed_frame, width = 500, height = 500, bd = 1,
                highlightthickness = 1, bg = 'alice blue')
w_canvas.pack()

w_canvas.create_text(250,35,text = "Weeding",font = ('Times',36))

w_canvas.create_line(175,55,335,55)
w_canvas.create_line(195,67,315,67)

q_report_button = Button(weed_frame, text = 'Quick Report',font = ('Helvetica',17),
                bg = 'MediumOrchid2', command=lambda : weeding(False))
q_report_button.pack()
q_report_button_window = w_canvas.create_window(250, 200, width = 330, height = 85, window=q_report_button)

f_report_button = Button(weed_frame, text = 'Full Report',font = ('Helvetica',17),
                bg = 'Cornflower blue', command=lambda : weeding(True))
f_report_button.pack()
f_report_button_window = w_canvas.create_window(250, 330, width = 330, height = 85, window=f_report_button)

return_button = Button(weed_frame, text = 'Return',font = ('Helvetica',17),
                bg = 'Red2', command=lambda : change_frame(weed_frame, f1))
return_button.pack()
return_button_window = w_canvas.create_window(60, 430, width = 90, height = 55, window=return_button)

q_button = Button(weed_frame, text = 'Quit',font = ('Helvetica',15),
                bg = 'Red2', command=lambda root=root:close(root))
q_button.pack()
q_button_window = w_canvas.create_window(460, 480, width = 60, height = 35, window=q_button)

#####################

root.mainloop() 
