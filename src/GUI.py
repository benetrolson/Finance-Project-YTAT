#This will be the set up for the menu using the GUI
import tkinter as tk
from tkinter import *
import time

root = tk.Tk()

root.title("FINANCE PROJECT")
root.configure(background="light grey")
root.minsize(900,300)
root.maxsize(1500,500)
root.geometry("1200x400+100+100")

name_var=tk.StringVar()
passw_var=tk.StringVar()
Entriescatagories=tk.StringVar()


#Here is the concept is to make pre loaded and planed areas where we will load with the diffrent labels and buttons
def truesignup():
    btn.place_forget()
    sign.place_forget()
    root.singuplabel = tk.Label(root, text=f"This is where you would have signed up but that has not been added yet", bg="Light grey", font=("Times new roman", 14, "bold"))
    root.singuplabel.place(relx=.5, rely=0, anchor="n")

    root.name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    root.name_entry.place(relx=0.55, rely=0.3, anchor="n")

    root.name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    root.name_label.place(relx=0.45, rely=0.3, anchor="n")

    root.passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    root.passw_entry.place(relx=0.55, rely=0.4, anchor="n")

    root.passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    root.passw_label.place(relx=0.45, rely=0.4, anchor="n")

    root.btn1 = tk.Button(root, text="Enter",command=signingup)
    root.btn1.place(relx=.5, rely=0.7, anchor="n")
def signingup():
    #What ever do to the document
    EnteriesGUI()
def SignupGUI():
    
    btn.place_forget()
    sign.place_forget()
    root.singuplabel = tk.Label(root, text=f"This is tempory text while we add the sign in function\n To go passed the username is Test1 and password is Test2", bg="Light grey", font=("Times new roman", 14, "bold"))
    root.singuplabel.place(relx=.5, rely=0, anchor="n")

    

    root.name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    root.name_entry.place(relx=0.55, rely=0.3, anchor="n")

    root.name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    root.name_label.place(relx=0.45, rely=0.3, anchor="n")

    root.passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    root.passw_entry.place(relx=0.55, rely=0.4, anchor="n")

    root.passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    root.passw_label.place(relx=0.45, rely=0.4, anchor="n")

    root.btn1 = tk.Button(root, text="Enter",command=submiting_password)
    root.btn1.place(relx=.5, rely=0.7, anchor="n")
def submiting_password():
    #Replace this with the sign in system that checks it
    root.bools = 0
    name=name_var.get()
    password=passw_var.get()
    if name == "Test1":
        root.bools += 1
    if password == "Test2":
        root.bools += 1
    if root.bools == 2:
        EnteriesGUI()
    else:
        root.wrg_label = tk.Label(root, text = 'Incorrect password or username', font = ('calibre',10,'bold'))
        root.wrg_label.place(relx=0.5, rely=0.2, anchor="n")
def EnteriesGUI():
    #Clearing
    root.singuplabel.place_forget()
    root.btn1.place_forget()
    root.name_entry.place_forget()
    root.name_label.place_forget()
    root.passw_entry.place_forget()
    root.passw_label.place_forget()
    root.singuplabel.place_forget()
    root.wrg_label.place_forget()

    #Replacing
    root.vent = tk.Button(root, text="View your entries")
    root.vent.place(relx=.35, rely=0.4, anchor="n")
    root.aent = tk.Button(root, text="Add an entry", command=addentriesGui)
    root.aent.place(relx=.45, rely=0.4, anchor="n")
    root.dent = tk.Button(root, text="Delete an entry", command=DeleteGui)
    root.dent.place(relx=.55, rely=0.4, anchor="n")
    root.sent = tk.Button(root, text="View a statistics", command=statisticspickerGui)
    root.sent.place(relx=.65, rely=0.4, anchor="n")
    


def statisticspickerGui():
    root.vent.place_forget()
    root.aent.place_forget()
    root.dent.place_forget()
    root.sent.place_forget()

    root.barbin = tk.Button(root, text="Bar Graph")
    root.barbin.place(relx=.35, rely=0.4, anchor="n")
    root.piebin = tk.Button(root, text="Pie-chart graph")
    root.piebin.place(relx=.45, rely=0.4, anchor="n")
    root.Exitbin = tk.Button(root, text="Go back", command=fixstatistcs)
    root.Exitbin.place(relx=.55, rely=0.4, anchor="n")
def fixstatistcs():
    root.barbin.place_forget()
    root.piebin.place_forget()
    root.Exitbin.place_forget()
    EnteriesGUI()
def fixguiaddons():
    root.incomebin.place_forget()
    root.Savbin.place_forget()
    root.extbin.place_forget()
    root.expcesbin.place_forget()

    EnteriesGUI()
def addentriesGui():
    root.vent.place_forget()
    root.aent.place_forget()
    root.dent.place_forget()
    root.sent.place_forget()

    root.incomebin = tk.Button(root, text="Income saving")
    root.incomebin.place(relx=.35, rely=0.4, anchor="n")
    root.Savbin = tk.Button(root, text="Savings")
    root.Savbin.place(relx=.45, rely=0.4, anchor="n")
    root.expcesbin = tk.Button(root, text="Expences")
    root.expcesbin.place(relx=.55, rely=0.4, anchor="n")
    root.extbin = tk.Button(root, text="Go back", command=fixguiaddons)
    root.extbin.place(relx=.45, rely=0.6, anchor="n")

def DeleteGui():
    root.vent.place_forget()
    root.aent.place_forget()
    root.dent.place_forget()
    root.sent.place_forget()

    root.incomebin = tk.Button(root, text="Income saving")
    root.incomebin.place(relx=.35, rely=0.4, anchor="n")
    root.Savbin = tk.Button(root, text="Savings")
    root.Savbin.place(relx=.45, rely=0.4, anchor="n")
    root.expcesbin = tk.Button(root, text="Expences")
    root.expcesbin.place(relx=.55, rely=0.4, anchor="n")
    root.extbin = tk.Button(root, text="Go back", command=fixguiaddons)
    root.extbin.place(relx=.45, rely=0.6, anchor="n")

    


#Here is the starting buttons
btn = tk.Button(root, text="Sign up", command=truesignup)
btn.place(relx=.53, rely=0.4, anchor="n")
root.wrg_label = tk.Label(root, text = '', font = ('calibre',10,'bold'))
sign = tk.Button(root, text="Sign in", command=SignupGUI)
sign.place(relx=.47, rely=0.4, anchor="n")
root.exiting = tk.Button(root, text="Exit program", command=root.destroy)
root.exiting.place(relx=.05, rely=0.05, anchor="n")








root.mainloop()