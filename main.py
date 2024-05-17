  # *********************************************************************************************
from tkinter import *
from tkinter import messagebox,ttk
import tkinter as tk
import os
import openpyxl as xl

# ********************************************************************************************
# Method section
def Add():
    acpwtcs = int(acpcstext.get())
    print(acpwtcs)
    acpwtamt = int(acpamttext.get())
    print(acpwtamt)
  
########################## Start Main Window Programm ##########################################

win = tk.Tk()
win.title("Staion PCDO")
# # Set window size
# window_width = win.winfo_width()
# window_height = win.winfo_height()

width= win.winfo_screenwidth()               
height= win.winfo_screenheight()               
win.geometry("%dx%d" % (width, height))

############################################################################################################
# Tital Lable 

titlelable = tk.Label(win,text='STATION PCDO ENTRY FORM',font=('New Times Roman',20,'bold'),
                      relief=GROOVE,padx=10,pady=10,bd=10,fg='dark slate blue')

titlelable.pack(fill=X,ipadx=5,ipady=5)

##########################################################################################################
# Station selection and search form

stnlable = ttk.Labelframe(win,)

stnelable = tk.Label(stnlable,text='Station Name ',font=('Times New Roman',12,'bold'),borderwidth=10,padx=20,pady=10)
stnelable.grid(row=0,column=0)

stncomb = ttk.Combobox(stnlable,)
stncomb.grid(row=0,column=1,padx=20)

period = ttk.Label(stnlable,text='Select Period',font=('Times New Roman',12,'bold'))
period.grid(row=0,column=2,padx=10)

periodchk = tk.Checkbutton(stnlable,text='I st ',font=('Times New Roman',12,'bold'))
periodchk.grid(row=0,column=3,padx=10)

periodchk = tk.Checkbutton(stnlable,text='II nd ',font=('Times New Roman',12,'bold'))
periodchk.grid(row=0,column=4,padx=10)

periodchk = tk.Checkbutton(stnlable,text='III rd ',font=('Times New Roman',12,'bold'))
periodchk.grid(row=0,column=5,padx=10)

addbutton = tk.Button(stnlable,text='ADD',padx=30,pady=6,command=Add,font=('Times New Roman',12,'bold'),
                      fg='brown',bg='light green')
addbutton.grid(row=0,column=6,padx=20)

srchtext = tk.Entry(stnlable,font=('Times New Roman',12,'bold'),relief=GROOVE)
srchtext.grid(row=0,column=7)

srchbutton = tk.Button(stnlable,text='Search',padx=30,pady=6,command=Add,font=('Times New Roman',12,'bold'),
                      fg='brown',bg='yellow')
srchbutton.grid(row=0,column=8,padx=20)
stnlable.pack()
##########################################################################################################
# Entry form
mainframe = tk.LabelFrame(win,text='Main Entry form',font=('New Times Roman',10,'bold'),
            fg='blue',padx=10,relief=GROOVE,border=10)

##############################################################################################################
#AC Local frame and Entry

acframe = tk.LabelFrame(mainframe,text='AC LOCAL',fg='green',font=('bold',10),relief=GROOVE,border=5) 

aclable=tk.Label(acframe,text='PWT',font=('New Times Roman',12,'bold'))
aclable.grid(row=0,column=0,columnspan=2)

acpcslable = tk.Label(acframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
acpcslable.grid(row=1,column=0)

acpcstext = tk.Entry(acframe,relief=GROOVE,width=10)
acpcstext.grid(row=1,column=1)

acpamtlable = tk.Label(acframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
acpamtlable.grid(row=2,column=0)

acpamttext = tk.Entry(acframe,relief=GROOVE,width=10)
acpamttext.grid(row=2,column=1)

acdflable=tk.Label(acframe,text='Difference',font=('New Times Roman',12,'bold'),pady=5)
acdflable.grid(row=3,column=0,columnspan=2)

acdcslable = tk.Label(acframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
acdcslable.grid(row=4,column=0)

acdcstext = tk.Entry(acframe,relief=GROOVE,width=10)
acdcstext.grid(row=4,column=1)

acdamtlable = tk.Label(acframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
acdamtlable.grid(row=5,column=0)

acamttext = tk.Entry(acframe,relief=GROOVE,width=10)
acamttext.grid(row=5,column=1)

acframe.grid(row=0,column=0,padx=10,pady=10,ipadx=5) # AC Frame close

################################################################################################################
#FC Local frame and Entry

fcframe = tk.LabelFrame(mainframe,text='FC ',fg='red',font=('bold',10),relief=GROOVE,border=5) 

fclable=tk.Label(fcframe,text='PWT',font=('New Times Roman',12,'bold'))
fclable.grid(row=0,column=0,columnspan=2)

fcpcslable = tk.Label(fcframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
fcpcslable.grid(row=1,column=0)

fcpcstext = tk.Entry(fcframe,relief=GROOVE,width=10)
fcpcstext.grid(row=1,column=1)

fcpamtlable = tk.Label(fcframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
fcpamtlable.grid(row=2,column=0)

fcpamttext = tk.Entry(fcframe,relief=GROOVE,width=10)
fcpamttext.grid(row=2,column=1)

fcdflable=tk.Label(fcframe,text='Difference',font=('New Times Roman',12,'bold'),pady=5)
fcdflable.grid(row=3,column=0,columnspan=2)

fcdcslable = tk.Label(fcframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
fcdcslable.grid(row=4,column=0)

fcdcstext = tk.Entry(fcframe,relief=GROOVE,width=10)
fcdcstext.grid(row=4,column=1)

fcdamtlable = tk.Label(fcframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
fcdamtlable.grid(row=5,column=0)

fcamttext = tk.Entry(fcframe,relief=GROOVE,width=10)
fcamttext.grid(row=5,column=1)

fcframe.grid(row=0,column=1,padx=10,pady=10,ipadx=5) # FC Frame close

#####################################################################################################################
#Mail Express frame and Entry

meframe = tk.LabelFrame(mainframe,text='M/E',fg='green',font=('bold',10),relief=GROOVE,border=5) 

melable=tk.Label(meframe,text='PWT',font=('New Times Roman',12,'bold'))
melable.grid(row=0,column=0,columnspan=2)

mepcslable = tk.Label(meframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
mepcslable.grid(row=1,column=0)

mepcstext = tk.Entry(meframe,relief=GROOVE,width=10)
mepcstext.grid(row=1,column=1)

mepamtlable = tk.Label(meframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
mepamtlable.grid(row=2,column=0)

mepamttext = tk.Entry(meframe,relief=GROOVE,width=10)
mepamttext.grid(row=2,column=1)

medflable=tk.Label(meframe,text='Difference',font=('New Times Roman',12,'bold'),pady=5)
medflable.grid(row=3,column=0,columnspan=2)

medcslable = tk.Label(meframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
medcslable.grid(row=4,column=0)

medcstext = tk.Entry(meframe,relief=GROOVE,width=10)
medcstext.grid(row=4,column=1)

medamtlable = tk.Label(meframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
medamtlable.grid(row=5,column=0)

meamttext = tk.Entry(meframe,relief=GROOVE,width=10)
meamttext.grid(row=5,column=1)

meframe.grid(row=0,column=5,padx=10,pady=10,ipadx=5) # ME Frame close

############################################################################################################
#IInd Local frame and Entry

iiframe = tk.LabelFrame(mainframe,text='IInd Ord',fg='red',font=('bold',10),relief=GROOVE,border=5) 

iilable=tk.Label(iiframe,text='PWT',font=('New Times Roman',12,'bold'))
iilable.grid(row=0,column=0,columnspan=2)

iipcslable = tk.Label(iiframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
iipcslable.grid(row=1,column=0)

iipcstext = tk.Entry(iiframe,relief=GROOVE,width=10)
iipcstext.grid(row=1,column=1)

iipamtlable = tk.Label(iiframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
iipamtlable.grid(row=2,column=0)

iipamttext = tk.Entry(iiframe,relief=GROOVE,width=10)
iipamttext.grid(row=2,column=1)

ubllable=tk.Label(iiframe,text='UBL',font=('New Times Roman',12,'bold'),pady=5)
ubllable.grid(row=3,column=0,columnspan=2)

ublcslable = tk.Label(iiframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
ublcslable.grid(row=4,column=0)

ublcstext = tk.Entry(iiframe,relief=GROOVE,width=10)
ublcstext.grid(row=4,column=1)

ublamtlable = tk.Label(iiframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
ublamtlable.grid(row=5,column=0)

ublamttext = tk.Entry(iiframe,relief=GROOVE,width=10)
ublamttext.grid(row=5,column=1)

iiframe.grid(row=0,column=2,padx=10,pady=10,ipadx=5) # iind orFrame close
###############################################################################################################
#Total Staff postion Local frame and Entry

totalframe = tk.LabelFrame(mainframe,text='TOTAL & STAFF POSITION',fg='green',font=('bold',10),relief=GROOVE,border=5) 

totallable=tk.Label(totalframe,text='Total',font=('New Times Roman',12,'bold'))
totallable.grid(row=0,column=0,columnspan=2)

totalcslable = tk.Label(totalframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
totalcslable.grid(row=1,column=0)

totalcstext = tk.Label(totalframe,relief=GROOVE,width=10,font=('New Times Roman',12,'bold'),fg='red')
totalcstext.grid(row=1,column=1)

totalamtlable = tk.Label(totalframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
totalamtlable.grid(row=2,column=0)

totalamttext = tk.Label(totalframe,relief=GROOVE,width=10,font=('New Times Roman',12,'bold'),fg='red')
totalamttext.grid(row=2,column=1)

stafflable=tk.Label(totalframe,text='Staff',font=('New Times Roman',12,'bold'),pady=5)
stafflable.grid(row=3,column=0,columnspan=2)

tstafflable = tk.Label(totalframe,text='STAFF',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
tstafflable.grid(row=4,column=0)

stafftext = tk.Entry(totalframe,relief=GROOVE,width=10)
stafftext.grid(row=4,column=1)

wdlable = tk.Label(totalframe,text='W/D ',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
wdlable.grid(row=5,column=0)

wdtext = tk.Entry(totalframe,relief=GROOVE,width=10)
wdtext.grid(row=5,column=1)

totalframe.grid(row=0,column=3,padx=10,pady=10,ipadx=5) # UBL and Staff Frame close
##############################################################################################################
#Littering and Smoking Local frame and Entry

ltframe = tk.LabelFrame(mainframe,text='LITTERING & SMOKING',fg='red',font=('bold',10),relief=GROOVE,border=5,padx=10) 

ltlable=tk.Label(ltframe,text='Littering',font=('New Times Roman',12,'bold'))
ltlable.grid(row=0,column=0,columnspan=2)

ltsmlable = tk.Label(ltframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
ltsmlable.grid(row=1,column=0)

lttext = tk.Entry(ltframe,relief=GROOVE,width=10)
lttext.grid(row=1,column=1)

ltamtlable = tk.Label(ltframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
ltamtlable.grid(row=2,column=0)

ltamttext = tk.Entry(ltframe,relief=GROOVE,width=10)
ltamttext.grid(row=2,column=1)

smlable=tk.Label(ltframe,text='Smoking',font=('New Times Roman',12,'bold'),pady=5)
smlable.grid(row=3,column=0,columnspan=2)

smcslable = tk.Label(ltframe,text='C/S',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,pady=10,bd=10)
smcslable.grid(row=4,column=0)

smcstext = tk.Entry(ltframe,relief=GROOVE,width=10)
smcstext.grid(row=4,column=1)

smamtlable = tk.Label(ltframe,text='AMOUNT',font=('New Times Roman',12,'bold'),
                   relief=FLAT,padx=10,bd=10)
smamtlable.grid(row=5,column=0)

smamttext = tk.Entry(ltframe,relief=GROOVE,width=10)
smamttext.grid(row=5,column=1)

ltframe.grid(row=0,column=4,padx=10) # LIttering and Smoking Frame close
#######################################################################################################

mainframe.pack(fill=X)  #Main Frame close

# Show entered data
dataframe= ttk.LabelFrame(win,text='Station wise Entered Data')
datashow = ttk.Treeview()
datashow.pack(fill=X)
dataframe.pack(fill=X)


win.mainloop()
