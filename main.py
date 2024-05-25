# *********************************************************************************************
from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk
import os
import openpyxl as xl
import pandas as pd
from datetime import datetime
import footer
from openpyxl import load_workbook, Workbook


# excelconn.load_workbook()
# excelconn.savefile()

# ************************** Combobox List integrete with Excelsheet ***************************

df = pd.read_excel('STN_PCDO.xlsx',sheet_name='STN_LIST')
stnlist = df.iloc[:,0].tolist()
################################################################################################
def clear():
    acpcs.delete(0,END)
    fcpcs.delete(0,END)
    iipcs.delete(0,END)
    ublcs.delete(0,END)
    mepcs.delete(0,END)
    acdcs.delete(0,END)
    fcdcs.delete(0,END)
    medcs.delete(0,END)
    ltcs.delete(0,END)
    smcs.delete(0,END)
    staff.delete(0,END)
    wd.delete(0,END)
    totalcs.config(text='')
    
    # Amount
    acpamt.delete(0,END)
    fcpamt.delete(0,END)
    iipamt.delete(0,END)
    ublamt.delete(0,END)
    mepamt.delete(0,END)
    acdamt.delete(0,END)
    fcdamt.delete(0,END)
    medamt.delete(0,END)
    ltamt.delete(0,END)
    smamt.delete(0,END)
    totalamt.config(text='')
    set_zero()
    stncomb.focus()

def set_zero():

    acpcs.insert(0,0)
    acpamt.insert(0,0)
    fcpcs.insert(0,0)
    fcpamt.insert(0,0)
    iipcs.insert(0,0)
    iipamt.insert(0,0)
    ublcs.insert(0,0)
    ublamt.insert(0,0)
    mepcs.insert(0,0)
    mepamt.insert(0,0)
    medcs.insert(0,0)
    medamt.insert(0,0)
    staff.insert(0,0)
    wd.insert(0,0)
    ltcs.insert(0,0)
    ltamt.insert(0,0)
    smcs.insert(0,0)
    smamt.insert(0,0)
    acdcs.insert(0,0)
    acdamt.insert(0,0)
    fcdcs.insert(0,0)
    fcdamt.insert(0,0)
# Method section
def show(*args):
    # Cases
    tcs=0
    acs= int(acpcs.get())
    fcs = int(fcpcs.get())
    iics = int(iipcs.get())
    ucs = int(ublcs.get())
    mec = int(mepcs.get())
    acdc = int(acdcs.get())
    fcdc = int(fcdcs.get())
    medc = int(medcs.get())
    
    tcs = acs+fcs+iics+mec+acdc+fcdc+medc+ucs
    
    totalcs.config(text=tcs)
    
    # Amount
    aca= int(acpamt.get())
    fca = int(fcpamt.get())
    iia = int(iipamt.get())
    ua = int(ublamt.get())
    mea = int(mepamt.get())
    acda = int(acdamt.get())
    fcda = int(fcdamt.get())
    meda = int(medamt.get())
    
    
    tamt = aca+fca+iia+mea+acda+fcda+meda+ua
    
    totalamt.config(text=tamt)
    
# def add():
#     tlcs=acpcs+fcpcs
    

def setradio():
    select_value = pradio.get()
    
########################## Start Main Window Programm ############################################
global acpcs,acdcs,fcpcs,fcdcs,iipcs,mepcs,medcs
global acdamt,acpamt,fcpamt,fcdamt,iipamt,mepamt,medamt

win = tk.Tk()
win.title("Staion PCDO")
width= win.winfo_screenwidth()               
height= win.winfo_screenheight()               
win.geometry("%dx%d" % (width, height))

###################################################################################################
# Tital Lable 

tk.Label(win,text='STATION PCDO ENTRY FORM',font=('New Times Roman',20,'bold'),relief=GROOVE,padx=10,
                      pady=1,bd=5,fg='dark slate blue',bg='sky blue').pack(fill=X,ipadx=5,ipady=2)


#####################################################################################################
# Station selection and search form

stnlable = ttk.Labelframe(win,)

tk.Label(stnlable,text='Station Name ',font=('Times New Roman',12,'bold'),
                     borderwidth=10,padx=20).grid(row=0,column=0)
cmbox= tk.StringVar()
stncomb = ttk.Combobox(stnlable,values=stnlist,textvariable=cmbox)
stncomb.grid(row=0,column=1,padx=10)
stncomb.set(stnlist[0])

tk.Label(stnlable,text='Select Period',font=('Times New Roman',12,'bold')).grid(row=0,column=2,padx=10)

pradio = tk.IntVar()
radio=tk.Radiobutton(stnlable,text='I st ',font=('Times New Roman',12,'bold'),value=1,
                           variable=pradio,command=setradio).grid(row=0,column=3,padx=10)

radio=tk.Radiobutton(stnlable,text='II nd ',font=('Times New Roman',12,'bold'),value=2,
                           variable=pradio,).grid(row=0,column=4,padx=10)

radio=tk.Radiobutton(stnlable,text='III rd ',font=('Times New Roman',12,'bold'),value=3,
                           variable=pradio).grid(row=0,column=5,padx=10)
pradio.set(1)

addbtn = tk.Button(stnlable,text='ADD',padx=10,pady=5,font=('Times New Roman',12,'bold'),
                      fg='brown',bg='light green').grid(row=0,column=6,padx=10,pady=10)

editbtn = tk.Button(stnlable,text='EDIT',padx=10,pady=5,font=('Times New Roman',12,'bold'),
                      fg='brown',bg='orange').grid(row=0,column=7,padx=10,pady=10)

tk.Entry(stnlable,font=('Times New Roman',12,'bold'),relief=GROOVE).grid(row=0,column=8,padx=10)

srchbutton = tk.Button(stnlable,text='Search',padx=10,pady=5,font=('Times New Roman',12,'bold'),
                      fg='brown',bg='yellow').grid(row=0,column=9,padx=10,pady=10)

clrhbutton = tk.Button(stnlable,text='CLEAR',padx=10,pady=5,font=('Times New Roman',12,'bold'),
                      fg='brown',bg='yellow',command=clear).grid(row=0,column=10,padx=10,pady=10)

stnlable.pack()
##########################################################################################################
# Entry form
mainframe = tk.LabelFrame(win,text='Main Entry form',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=5)

##############################################################################################################
#AC Local frame and Entry

acframe = tk.LabelFrame(mainframe,text='AC LOCAL',fg='green',font=('bold',10),relief=GROOVE,border=5)

tk.Label(acframe,text='PWT',font=('New Times Roman',12,'bold')).grid(row=0,column=0,columnspan=2)

tk.Label(acframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=1,column=0)

acpcs = tk.Entry(acframe,relief=GROOVE,width=10)
acpcs.grid(row=1,column=1)
acpcs.insert(0,0)
acpcs.bind("<KeyRelease>",show)

tk.Label(acframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=2,column=0)

acpamt = tk.Entry(acframe,relief=GROOVE,width=10)
acpamt.grid(row=2,column=1)
acpamt.insert(0,0)
acpamt.bind("<KeyRelease>",show)

tk.Label(acframe,text='Difference',font=('New Times Roman',12,'bold'),pady=5).grid(row=3,column=0,columnspan=2)

tk.Label(acframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=4,column=0)

acdcs = tk.Entry(acframe,relief=GROOVE,width=10)
acdcs.grid(row=4,column=1)
acdcs.insert(0,0)
acdcs.bind("<KeyRelease>",show)

tk.Label(acframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=5,column=0)

acdamt= tk.Entry(acframe,relief=GROOVE,width=10)
acdamt.grid(row=5,column=1)
acdamt.insert(0,0)
acdamt.bind("<KeyRelease>",show)

acframe.grid(row=0,column=0,padx=10,pady=5,ipadx=5) # AC Frame close

################################################################################################################
#FC Local frame and Entry

fcframe = tk.LabelFrame(mainframe,text='FC ',fg='red',font=('bold',10),relief=GROOVE,border=5) 

tk.Label(fcframe,text='PWT',font=('New Times Roman',12,'bold'),
                 ).grid(row=0,column=0,columnspan=2)

tk.Label(fcframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=1,column=0)

fcpcs = tk.Entry(fcframe,relief=GROOVE,width=10)
fcpcs.grid(row=1,column=1)
fcpcs.insert(0,0)
fcpcs.bind("<KeyRelease>",show)

tk.Label(fcframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=2,column=0)

fcpamt = tk.Entry(fcframe,relief=GROOVE,width=10)
fcpamt.grid(row=2,column=1)
fcpamt.insert(0,0)
fcpamt.bind("<KeyRelease>",show)

tk.Label(fcframe,text='Difference',font=('New Times Roman',12,'bold'),pady=5
                   ).grid(row=3,column=0,columnspan=2)

tk.Label(fcframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=4,column=0)

fcdcs = tk.Entry(fcframe,relief=GROOVE,width=10)
fcdcs.grid(row=4,column=1)
fcdcs.insert(0,0)
fcdcs.bind("<KeyRelease>",show)

tk.Label(fcframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=5,column=0)

fcdamt = tk.Entry(fcframe,relief=GROOVE,width=10)
fcdamt.grid(row=5,column=1)
fcdamt.insert(0,0)
fcdamt.bind("<KeyRelease>",show)

fcframe.grid(row=0,column=1,padx=10,pady=5,ipadx=5) # FC Frame close

#####################################################################################################################
#IInd Local frame and Entry

iiframe = tk.LabelFrame(mainframe,text='IInd Ord',fg='red',font=('bold',10),relief=GROOVE,border=5) 

tk.Label(iiframe,text='PWT',font=('New Times Roman',12,'bold')).grid(row=0,column=0,columnspan=2)

tk.Label(iiframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=1,column=0)

iipcs = tk.Entry(iiframe,relief=GROOVE,width=10)
iipcs.grid(row=1,column=1)
iipcs.insert(0,0)
iipcs.bind("<KeyRelease>",show)

tk.Label(iiframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=2,column=0)

iipamt = tk.Entry(iiframe,relief=GROOVE,width=10)
iipamt.grid(row=2,column=1)
iipamt.insert(0,0)
iipamt.bind("<KeyRelease>",show)

tk.Label(iiframe,text='UBL',font=('New Times Roman',12,'bold'),pady=5
         ).grid(row=3,column=0,columnspan=2)

tk.Label(iiframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=4,column=0)

ublcs = tk.Entry(iiframe,relief=GROOVE,width=10)
ublcs.grid(row=4,column=1)
ublcs.insert(0,0)
ublcs.bind("<KeyRelease>",show)

tk.Label(iiframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=5,column=0)

ublamt = tk.Entry(iiframe,relief=GROOVE,width=10)
ublamt.grid(row=5,column=1)
ublamt.insert(0,0)
ublamt.bind("<KeyRelease>",show)

iiframe.grid(row=0,column=2,padx=10,pady=5,ipadx=5) # iind orFrame close
###############################################################################################################
#Total Staff postion Local frame and Entry

totalframe = tk.LabelFrame(mainframe,text='TOTAL & STAFF POSITION',fg='green',font=('bold',10),relief=GROOVE,border=5) 

tk.Label(totalframe,text='Total',font=('New Times Roman',12,'bold')).grid(row=0,column=0,columnspan=2)

tk.Label(totalframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=1,column=0)

totalcs = tk.Label(totalframe,relief=GROOVE,width=10,font=('New Times Roman',12,'bold'),
                   fg='red')
totalcs.grid(row=1,column=1)
acpcs.bind("<KeyRelease>",show)

tk.Label(totalframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=2,column=0)

totalamt = tk.Label(totalframe,relief=GROOVE,width=10,font=('New Times Roman',12,'bold'),
                    fg='red')
totalamt.grid(row=2,column=1)

tk.Label(totalframe,text='Staff',font=('New Times Roman',12,'bold'),pady=5
                          ).grid(row=3,column=0,columnspan=2)

tk.Label(totalframe,text='STAFF',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=4,column=0)

staff = tk.Entry(totalframe,relief=GROOVE,width=10)
staff.grid(row=4,column=1)
staff.insert(0,0)

tk.Label(totalframe,text='W/D ',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=5,column=0)

wd = tk.Entry(totalframe,relief=GROOVE,width=10)
wd.grid(row=5,column=1)
wd.insert(0,0)

totalframe.grid(row=0,column=3,padx=10,pady=10,ipadx=5) # UBL and Staff Frame close
##############################################################################################################
#Littering and Smoking Local frame and Entry

ltframe = tk.LabelFrame(mainframe,text='LITTERING & SMOKING',fg='red',font=('bold',10),relief=GROOVE,border=5,padx=10) 

tk.Label(ltframe,text='Littering',font=('New Times Roman',12,'bold')).grid(row=0,column=0,columnspan=2)

tk.Label(ltframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=1,column=0)

ltcs = tk.Entry(ltframe,relief=GROOVE,width=10)
ltcs.grid(row=1,column=1)
ltcs.insert(0,0)

tk.Label(ltframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=2,column=0)

ltamt = tk.Entry(ltframe,relief=GROOVE,width=10)
ltamt.grid(row=2,column=1)
ltamt.insert(0,0)

tk.Label(ltframe,text='Smoking',font=('New Times Roman',12,'bold'),pady=5).grid(row=3,column=0,columnspan=2)

tk.Label(ltframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=4,column=0)

smcs = tk.Entry(ltframe,relief=GROOVE,width=10)
smcs.grid(row=4,column=1)
smcs.insert(0,0)

tk.Label(ltframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=5,column=0)

smamt = tk.Entry(ltframe,relief=GROOVE,width=10)
smamt.grid(row=5,column=1)
smamt.insert(0,0)

ltframe.grid(row=0,column=4,padx=10) # LIttering and Smoking Frame close
#######################################################################################################
#Mail Express frame and Entry

meframe = tk.LabelFrame(mainframe,text='M/E',fg='green',font=('bold',10),relief=GROOVE,border=5) 

tk.Label(meframe,text='PWT',font=('New Times Roman',12,'bold')).grid(row=0,column=0,columnspan=2)

tk.Label(meframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=1,column=0)

mepcs = tk.Entry(meframe,relief=GROOVE,width=10)
mepcs.grid(row=1,column=1)
mepcs.insert(0,0)
mepcs.bind("<KeyRelease>",show)

tk.Label(meframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=2,column=0)

mepamt = tk.Entry(meframe,relief=GROOVE,width=10)
mepamt.grid(row=2,column=1)
mepamt.insert(0,0)
mepamt.bind("<KeyRelease>",show)

tk.Label(meframe,text='Difference',font=('New Times Roman',12,'bold'),
                   pady=5).grid(row=3,column=0,columnspan=2)

tk.Label(meframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10).grid(row=4,column=0)

medcs = tk.Entry(meframe,relief=GROOVE,width=10)
medcs.grid(row=4,column=1)
medcs.insert(0,0)
medcs.bind("<KeyRelease>",show)

tk.Label(meframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10).grid(row=5,column=0)

medamt = tk.Entry(meframe,relief=GROOVE,width=10)
medamt.grid(row=5,column=1)
medamt.insert(0,0)
medamt.bind("<KeyRelease>",show)

meframe.grid(row=0,column=5,padx=10,pady=10,ipadx=5) # ME Frame close

############################################################################################################
mainframe.pack()  #Main Frame close

################################# Summery ##################################################

summryframe = tk.LabelFrame(win,text='SUMMERY',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=5)

suburbanframe = tk.LabelFrame(summryframe,text='Suburban',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=5)

tk.Label(suburbanframe,text='Total C/S',font=('New Times Roman',12,'bold')).grid(row=0,column=0)

tk.Label(suburbanframe,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=10).grid(row=0,column=1)

tk.Label(suburbanframe,text='Total Amt',font=('New Times Roman',12,'bold')).grid(row=1,column=0)

tk.Label(suburbanframe,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=10).grid(row=1,column=1)

suburbanframe.grid(row=0,column=0,padx=2,ipady=5) # Suburban Close

mainlineframe = tk.LabelFrame(summryframe,text='Mainline',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=5)

tk.Label(mainlineframe,text='Total C/S',font=('New Times Roman',12,'bold')).grid(row=0,column=0)

tk.Label(mainlineframe,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=10).grid(row=0,column=1)

tk.Label(mainlineframe,text='Total Amt',font=('New Times Roman',12,'bold')).grid(row=1,column=0)

tk.Label(mainlineframe,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=10).grid(row=1,column=1)

mainlineframe.grid(row=0,column=1,padx=2,ipady=5) # Main line close

litteringframe = tk.LabelFrame(summryframe,text='Littering',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=5)

tk.Label(litteringframe,text='Total C/S',font=('New Times Roman',12,'bold')).grid(row=0,column=0)

tk.Label(litteringframe,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=6).grid(row=0,column=1)

tk.Label(litteringframe,text='Total Amt',font=('New Times Roman',12,'bold')).grid(row=1,column=0)

tk.Label(litteringframe,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=6).grid(row=1,column=1)

litteringframe.grid(row=0,column=2,padx=2,ipady=5) #Littering close

smokingframe = tk.LabelFrame(summryframe,text='Smoking',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=5)

tk.Label(smokingframe,text='Total C/S',font=('New Times Roman',12,'bold')).grid(row=0,column=0)

tk.Label(smokingframe,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=5).grid(row=0,column=1)

tk.Label(smokingframe,text='Total Amt',font=('New Times Roman',12,'bold')).grid(row=1,column=0)

tk.Label(smokingframe,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=5).grid(row=1,column=1)

smokingframe.grid(row=0,column=3,padx=2,ipady=5)  # Smoking close

grandtotal = tk.LabelFrame(summryframe,text='Grand Total',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=5)

tk.Label(grandtotal,text='Total C/S',font=('New Times Roman',12,'bold')).grid(row=0,column=0)

tk.Label(grandtotal,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=10).grid(row=0,column=1)

tk.Label(grandtotal,text='Total Amt',font=('New Times Roman',12,'bold')).grid(row=1,column=0)

tk.Label(grandtotal,text='',font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5,bd=3,width=10).grid(row=1,column=1)

grandtotal.grid(row=0,column=4,padx=5,ipady=5) # Grand Total close

slistframe = tk.LabelFrame(summryframe,text='STN Periodical Not received',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=5)

slist = tk.Listbox(slistframe,width=20,height=5)
slist.pack()

countlist = tk.Label(slistframe,text='',width=10,bd=2,font=('New Times Roman',12,'bold'),
                   relief=GROOVE,padx=10,pady=5)
countlist.pack()


slistframe.grid(row=0,column=5,padx=2)

summryframe.pack(ipadx=2,ipady=3) # Summery close

######################################################################################################
footer.footer( root=win)

win.mainloop()  # Main Loop close

######################################################################################################
