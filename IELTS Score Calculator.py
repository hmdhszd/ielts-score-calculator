#! /usr/bin/python3
#! /usr/bin/env python3

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
import os



#----------------------------------------------------------


class Person:
    def __init__(self, fname, lname, LISTENING,READING,WRITING,SPEAKING ):
        self.fname = fname
        self.lname = lname
        self.LISTENING = LISTENING
        self.READING = READING
        self.WRITING = WRITING
        self.SPEAKING = SPEAKING




#----------------------------------------------------------


def add_DB_to_Listbox():
    list_of_files_in_DB = os.listdir("DB")
    print(list_of_files_in_DB)
    listbox.delete(0, END)
    for i in (list_of_files_in_DB):
        listbox.insert(END,i)
        
    




#----------------------------------------------------------



#create windows and items and input boxes:

window = Tk()
window.title("IELTS Score Calculator")
window.geometry('900x700')



firstheader = Label(window, text="Add info of each person :", font=("Arial Bold", 15))
firstheader.grid(column=0, row=0)




stname = Label(window, text="First name: ")
stname.grid(column=1, row=2)
fnametxt = Entry(window,width=15)
fnametxt.grid(column=2, row=2)


stlname = Label(window, text="Last name: ")
stlname.grid(column=3, row=2)
lnametxt = Entry(window,width=15)
lnametxt.grid(column=4, row=2)








titre1 = Label(window, text="Enter scores : ")
titre1.grid(column=1, row=6)



LISTENING = Label(window, text="LISTENING :")
LISTENING.grid(column=1, row=7)
LISTENINGtxt = Entry(window,width=15)
LISTENINGtxt.grid(column=1, row=8)



READING = Label(window, text="READING :")
READING.grid(column=2, row=7)
READINGtxt = Entry(window,width=15)
READINGtxt.grid(column=2, row=8)



WRITING = Label(window, text="WRITING :")
WRITING.grid(column=3, row=7)
WRITINGtxt = Entry(window,width=15)
WRITINGtxt.grid(column=3, row=8)



SPEAKING = Label(window, text="SPEAKING :")
SPEAKING.grid(column=4, row=7)
SPEAKINGtxt = Entry(window,width=15)
SPEAKINGtxt.grid(column=4, row=8)






#----------------------------------------------------------












#txt = scrolledtext.ScrolledText(window,width=60,height=25)
#txt.place(x=500, y=360)






#----------------------------------------------------------
#what happens when we click on listbox items:

def CurSelet(evt):
    how_many_courses = 0
    total_of_notes = 0

    value=str((listbox.get(ANCHOR)))
    #txt.delete('1.0', END)
    

    txt.insert(INSERT,'\nStudent ID:   ')
    txt.insert(INSERT,value)
    txt.insert(INSERT,'\n\nFirst name: ')
    txt.insert(INSERT,allstudents[value][0])
    txt.insert(INSERT,'     Last name: ')
    txt.insert(INSERT,allstudents[value][1])
    txt.insert(INSERT,'\n\n  Birthday: ')
    txt.insert(INSERT,allstudents[value][2])
    txt.insert(INSERT,'\n  Grade: ')
    txt.insert(INSERT,allstudents[value][3])
    txt.insert(INSERT,'\n\n  Scores: ')
    
    if allstudents[value][4][0]:
        total_of_notes = total_of_notes + int(allstudents[value][4][0])
        how_many_courses +=1
        txt.insert(INSERT,'\n     Art: ')
        txt.insert(INSERT,allstudents[value][4][0])
    
    if allstudents[value][4][1]:
        total_of_notes = total_of_notes + int(allstudents[value][4][1])
        how_many_courses +=1
        txt.insert(INSERT,'\n     Mathematics: ')
        txt.insert(INSERT,allstudents[value][4][1])
    
    if allstudents[value][4][2]:
        total_of_notes = total_of_notes + int(allstudents[value][4][2])
        how_many_courses +=1
        txt.insert(INSERT,'\n     Music: ')
        txt.insert(INSERT,allstudents[value][4][2])
    
    if allstudents[value][4][3]:
        total_of_notes = total_of_notes + int(allstudents[value][4][3])
        how_many_courses +=1
        txt.insert(INSERT,'\n     Dance: ')
        txt.insert(INSERT,allstudents[value][4][3])
    
    if allstudents[value][4][4]:
        total_of_notes = total_of_notes + int(allstudents[value][4][4])
        how_many_courses +=1
        txt.insert(INSERT,'\n     Physical Science: ')
        txt.insert(INSERT,allstudents[value][4][4])
    
    if allstudents[value][4][5]:
        total_of_notes = total_of_notes + int(allstudents[value][4][5])
        how_many_courses +=1
        txt.insert(INSERT,'\n     EnglishLiterature: ')
        txt.insert(INSERT,allstudents[value][4][5])
    
    if allstudents[value][4][6]:
        total_of_notes = total_of_notes + int(allstudents[value][4][6])
        how_many_courses +=1
        txt.insert(INSERT,'\n     Chemistry: ')
        txt.insert(INSERT,allstudents[value][4][6])
    
    if allstudents[value][4][7]:
        total_of_notes = total_of_notes + int(allstudents[value][4][7])
        how_many_courses +=1
        txt.insert(INSERT,'\n     French: ')
        txt.insert(INSERT,allstudents[value][4][7])
    txt.insert(INSERT,'\n\n          Total of the selected courses: ')
    txt.insert(INSERT,how_many_courses)
    txt.insert(INSERT,'\n\n          Average: ')
    txt.insert(INSERT,(total_of_notes/how_many_courses))




#----------------------------------------------------------









#----------------------------------------------------------


lbl = Label(window,text = "Added items :")
lbl.place(x=15, y=340)

search_box = Entry(window,width=15)
search_box.place(x=110, y=338)


listbox = Listbox(window,width=60,height=24)
listbox.place(x=11, y=360)
listbox.bind('<<ListboxSelect>>',CurSelet)

add_DB_to_Listbox()



#----------------------------------------------------------












#----------------------------------------------------------
#what happens when we click on ADD button


def clicked():
    ready_to_add = True
    
    #txt.delete('1.0', END)

    if fnametxt.get():
        pass
    else:
        messagebox.askretrycancel('You have to fill all of the items !','Please enter First Name')
        ready_to_add = False


    if lnametxt.get():
        pass
    else:
        messagebox.askretrycancel('You have to fill all of the items !','Please enter Last Name')
        ready_to_add = False


    if LISTENINGtxt.get():
        pass
    else:
        messagebox.askretrycancel('You have to fill all of the items !','Please enter LISTENING score')
        ready_to_add = False

    if READINGtxt.get():
        pass
    else:
        messagebox.askretrycancel('You have to fill all of the items !','Please enter READING score')
        ready_to_add = False

    if WRITINGtxt.get():
        pass
    else:
        messagebox.askretrycancel('You have to fill all of the items !','Please enter WRITING score')
        ready_to_add = False

    if SPEAKINGtxt.get():
        pass
    else:
        messagebox.askretrycancel('You have to fill all of the items !','Please enter SPEAKING score')
        ready_to_add = False
        


    global xxx
    xxx = ready_to_add
    
    if (xxx):
        x = Person(fnametxt.get(), lnametxt.get(), LISTENINGtxt.get(), READINGtxt.get(), WRITINGtxt.get(), SPEAKINGtxt.get() )

        try:
            newfile = open('DB/'+x.fname + " " + x.lname ,"x")
        except FileExistsError:
            messagebox.askretrycancel("This name is already added to the data base." , "Please enter another name.")
        else:
            newfile.write(x.fname + "\n")
            newfile.write(x.lname + "\n")
            newfile.write(x.LISTENING + "\n")
            newfile.write(x.READING + "\n")
            newfile.write(x.WRITING + "\n")
            newfile.write(x.SPEAKING + "\n")
            newfile.close()
            messagebox.askretrycancel("Congrats !" , "This entry was added to DataBase.")

        
        add_DB_to_Listbox()
        
        
        
        




    #Empty the input boxes after add a student
    #stnametxt.configure(text= ' ')
    #stlnametxt.configure(text= ' ')
    #studentidtxt.configure(text= ' ')


#----------------------------------------------------------


btn = Button(window, text="Add", command=clicked)
btn.grid(column=5, row=8)

 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 

window.mainloop()