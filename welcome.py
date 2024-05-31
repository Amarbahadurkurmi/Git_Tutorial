from tkinter import *
from tkinter import messagebox,ttk,Menu
import tkinter as tk
import os
import openpyxl as xl
import pandas as pd
from datetime import datetime,timedelta
import menu
from PIL import Image, ImageTk


# ******************************** Main Window Start ****************************************
win = tk.Tk()
win.title("Staion PCDO")
width= win.winfo_screenwidth()               
height= win.winfo_screenheight()               
win.geometry("%dx%d" % (width, height))
menu.menub(root=win,tk=tk,)

def resize_image(image, max_width, max_height):
    # Calculate the ratio to maintain aspect ratio
    width_ratio = max_width / image.width
    height_ratio = max_height / image.height
    new_ratio = min(width_ratio, height_ratio)
    
    # Calculate new dimensions
    new_width = int(image.width * new_ratio)
    new_height = int(image.height * new_ratio)
    return image.resize((new_width, new_height))
#########################################################################################

winframe= tk.Frame(win,bd=5,bg='deep sky blue')

imageframe= tk.Frame(winframe,)

frame1=tk.Label(imageframe, text="")
# Specify the desired width and height
max_width = 250
max_height = 200

image = Image.open('akam.jpg')
resized_image = resize_image(image, max_width, max_height)
# Convert the resized image to a Tkinter-compatible image
photo1 = ImageTk.PhotoImage(resized_image)

# photo = ImageTk.PhotoImage(image)
tk.Label(frame1,image=photo1,justify=CENTER).pack(padx=50,expand=TRUE)

frame1.grid(row=0,column=0)


frame2=tk.Label(imageframe, text="")
tk.Label(frame2,text=('WELCOME'+'\n'+'TICKET CHECKHING SECTION'+'\n'+' MUMBAI DIVISION')
         ,font=('Times',30,'bold'),fg='blue').pack(fill=BOTH)

tk.Label(frame2,text=('The Intergration Module of PCDO and MCDO')
         ,font=('Times',15,'bold'),fg='deep sky blue').pack(padx=50,expand=TRUE)

frame2.grid(row=0,column=1)


frame3=tk.Label(imageframe, text="")
# Specify the desired width and height
max_width = 250
max_height = 200

image = Image.open('crlogo.jpg')
resized_image = resize_image(image, max_width, max_height)
# Convert the resized image to a Tkinter-compatible image
photo = ImageTk.PhotoImage(resized_image)

# photo = ImageTk.PhotoImage(image)
tk.Label(frame3,image=photo,).pack(padx=50,expand=TRUE)

frame3.grid(row=0,column=2)

imageframe.pack(fill=X,)

############################################ crousel image in frame ########################
croselframe = tk.Frame(winframe,)


image = Image.open('vande.jpg')
resized_image = resize_image(image, max_width, max_height)
# Convert the resized image to a Tkinter-compatible image
photo2 = ImageTk.PhotoImage(image)

image_label = tk.Label(croselframe,image=photo2)
max_width = 700
max_height = 500

image_label.pack(fill=X,padx=20,pady=20,expand=TRUE)

croselframe.pack(fill=X)
winframe.pack(fill=BOTH,expand=TRUE,padx=10,pady=10)


win.mainloop()  # Main Loop close