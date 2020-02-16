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
    def overal(self):
            return((int(self.LISTENING)+int(self.READING)+int(self.WRITING)+int(self.SPEAKING))/4)
        
        




#----------------------------------------------------------


def add_DB_to_Listbox():
    list_of_files_in_DB = os.listdir("DB")
    listbox.delete(0, END)
    for i in (list_of_files_in_DB):
        listbox.insert(END,i)
        
    




#----------------------------------------------------------



#create windows and items and input boxes:

window = Tk()
window.title("IELTS Score Calculator")
window.geometry('800x400')



firstheader = Label(window, text="Add info of each person :", font=("Arial Bold", 15))
firstheader.place(x=15, y=20)




stname = Label(window, text="First name: ")
stname.place(x=15, y=50)
fnametxt = Entry(window,width=15)
fnametxt.place(x=15, y=70)


stlname = Label(window, text="Last name: ")
stlname.place(x=15, y=100)
lnametxt = Entry(window,width=15)
lnametxt.place(x=15, y=120)








titre1 = Label(window, text="Enter scores : ")
titre1.place(x=15, y=150)



LISTENING = Label(window, text="LISTENING :")
LISTENING.place(x=15, y=170)
LISTENINGtxt = Entry(window,width=15)
LISTENINGtxt.place(x=15, y=190)



READING = Label(window, text="READING :")
READING.place(x=15, y=220)
READINGtxt = Entry(window,width=15)
READINGtxt.place(x=15, y=240)



WRITING = Label(window, text="WRITING :")
WRITING.place(x=15, y=270)
WRITINGtxt = Entry(window,width=15)
WRITINGtxt.place(x=15, y=290)



SPEAKING = Label(window, text="SPEAKING :")
SPEAKING.place(x=15, y=320)
SPEAKINGtxt = Entry(window,width=15)
SPEAKINGtxt.place(x=15, y=340)






#----------------------------------------------------------












#txt = scrolledtext.ScrolledText(window,width=60,height=25)
#txt.place(x=500, y=360)






#----------------------------------------------------------
#what happens when we click on listbox items:

def CurSelet(evt):
    value=str((listbox.get(ANCHOR)))
    with open('DB/'+value, 'r') as selectedfile:
        x = Person(selectedfile.readline(), selectedfile.readline(), selectedfile.readline(), selectedfile.readline(), selectedfile.readline(), selectedfile.readline() )
        messagebox.showinfo(x.fname + x.lname, "LISTENING :" + x.LISTENING +  "READING :" + x.READING + "WRITING :" + x.WRITING + "SPEAKING :" + x.SPEAKING + "Overal :" + str(x.overal()))




#----------------------------------------------------------



def search():
    try:
        with open('DB/'+search_box.get(), 'r') as selectedfile:
            x = Person(selectedfile.readline(), selectedfile.readline(), selectedfile.readline(), selectedfile.readline(), selectedfile.readline(), selectedfile.readline() )
            messagebox.showinfo(x.fname + x.lname, "LISTENING :" + x.LISTENING +  "READING :" + x.READING + "WRITING :" + x.WRITING + "SPEAKING :" + x.SPEAKING + "Overal :" + str(x.overal()))
    except FileNotFoundError as error:
        messagebox.showinfo(error, " Please  enter  a  full  name : (Name Familyname)       Or select from the items is the list !")




#----------------------------------------------------------


lbl = Label(window,text = "Search in the items :")
lbl.place(x=350, y=50)

search_box = Entry(window,width=15)
search_box.place(x=500, y=48)

searchbtn = Button(window, text="Search", command=search)
searchbtn.place(x=650, y=45)


listbox = Listbox(window,width=48,height=14)
listbox.place(x=350, y=100)
listbox.bind('<<ListboxSelect>>',CurSelet)

add_DB_to_Listbox()



#----------------------------------------------------------












#----------------------------------------------------------
#what happens when we click on ADD button


def clicked():
    ready_to_add = True



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
            
            try:
                x.overal()
            except (ValueError,UnboundLocalError) :
                messagebox.askretrycancel('Only numbers are allowed in the Score boxes !','Please enter ONLY NUMBER !')
                os.remove('DB/'+x.fname + " " + x.lname)
            
            else:
                messagebox.showinfo("Congrats !" , "This entry was added to the DataBase.")
                
            newfile.close()
        
        

        
        
        add_DB_to_Listbox()
    








#----------------------------------------------------------


btn = Button(window, text="Add =>", command=clicked)
btn.place(x=200, y=337)

 
 
 
 
 
 
 
 
 

 
 
 
 
 
 
 
 
 

window.mainloop()