#database
from tkinter import *

  
def get_records():
    f = open("database.txt","r")
    i = 1
    for l in f:
        globals()["rec" + str(i)] = l #makes a new variable counting up each loop
        i += 1 #changes the var from rec1 to rec2
    f.close()
    return {'rec1':rec1, 'rec2':rec2, 'rec3':rec3, 'rec4':rec4, 'rec5': rec5,
            'rec6':rec6, 'rec7':rec7, 'rec8':rec8, 'rec9':rec9, 'rec10': rec10,
            'rec11':rec11, 'rec12':rec12, 'rec13':rec13, 'rec14':rec14, 'rec15': rec15,
            'rec16':rec16, 'rec17':rec17, 'rec18':rec18, 'rec19':rec19, 'rec20': rec20,
            'rec21':rec21, 'rec22':rec22, 'rec23':rec23, 'rec24':rec24, 'rec25': rec25
            }
    #Each of the records are returned as a dictonary so
    #you can return multiple variables at once

    #returns records as a string


def list_records():
    f = open("database.txt","r")
    next(f) #skips first line
    i = 1
    for l in f:
        globals()["list" + str(i)] = [] #makes a new variable counting up each loop
        globals()["list" + str(i)] = globals()["list" + str(i)]+l.split(":")
        d = globals()["list" + str(i)][5].rstrip() #gets rid of \n at the end
        globals()["list" + str(i)][5] = int(d)
        globals()["list" + str(i)][0] = int(globals()["list" + str(i)][0])
        #separates record into each element
        i += 1
    f.close()
    list0 = ['ID','ISBN',' Title','Author','Purchase Date','Member ID']
    return {'list1':list1, 'list2':list2, 'list3':list3, 'list4':list4, 'list5': list5,
            'list6':list6, 'list7':list7, 'list8':list8, 'list9':list9, 'list10': list10,
            'list11':list11, 'list12':list12, 'list13':list13, 'list14':list14, 'list15': list15,
            'list16':list16, 'list17':list17, 'list18':list18, 'list19':list19, 'list20': list20,
            'list21':list21, 'list22':list22, 'list23':list23, 'list24':list24, 'list25': list25,
            'list0':list0}

    #returns records as a list split up by their elements

def list_logs():
    f = open("logfile.txt","r")
    i = 1
    logs = {}
    for l in f:
        globals()["log" + str(i)] = []
        globals()["log" + str(i)] = globals()["log" + str(i)]+l.split(":")
        d = globals()["log" + str(i)][1].rstrip()
        globals()["log" + str(i)][1] = int(d)
        logs["log"+str(i)] = globals()["log"+str(i)]
        #assigns a dictionary key to the list variable
        i += 1
    f.close()
    return logs

def write_records(row,column, value):
    lists = list_records()
    lists["list" + str(row)][column] = str(value)
    f = open("database.txt","w")
    for i in range(0,26):
        line = lists["list" + str(i)]
        line1 = [str(j) for j in line]
        #just makes every element in the list a string
        f.write(':'.join(line1)+'\n')
    f.close()
        
def write_log(name):
    log = list_logs()
    for i in range(1,15):
        if log["log"+str(i)][0].lower() == name.lower():
            #checks the name to the names in the log file
            log["log"+str(i)][1] +=1
            #adds 1 to returned value in the log file
        else:
            pass
    f = open("logfile.txt","w")
    for i in range(1,15):
        line = log["log"+str(i)]
        line1 = [str(j) for j in line]
        f.write(':'.join(line1)+'\n')
    f.close()


