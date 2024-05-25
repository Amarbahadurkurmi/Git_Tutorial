import tkinter as tk
from datetime import datetime
from tkinter import *

# global datelbl
def update_time():
    global datelbl
    # Get the current date and time
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    # Update the label with the current date and time
    datelbl.config(text=current_time)
    
    # Schedule the update_time function to be called again after 1000 milliseconds (1 second)
    datelbl.after(1000, update_time)
    
    
def footer(root):
    global datelbl
    cpframe = tk.LabelFrame(root,)
    copyrightlbl = tk.Label(cpframe,text='© 2024 CSDN Technology',font=('New Times Roman',10,'bold'),
                                fg='red',justify=LEFT,padx=200).grid(row=0,column=0)

    datelbl = tk.Label(cpframe,font=('New Times Roman',10,'bold'),justify=RIGHT,padx=600)
    datelbl.grid(row=0,column=1)
    datelbl.config(text=update_time())
    cpframe.pack(pady=2,fill=X)
    
    