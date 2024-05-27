import tkinter as tk
from tkinter import *
import pandas as pd
from tkinter import ttk, messagebox


global subcslbl
# Function to load data from Excel and calculate the sum for a specific column
def load_and_sum_column():
    try:
        # Load the Excel file
        df = pd.read_excel('stnpcdo.xlsx')
    except FileNotFoundError:
        messagebox.showerror("Error", "The file 'data.xlsx' was not found.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return

    # # Get the column name from the Entry widget
    # column_name = column_entry.get()
    
    # if column_name not in df.columns:
    #     messagebox.showerror("Error", f"The column '{column_name}' was not found in the Excel sheet.")
    #     return
    
    # Calculate the sum for the specific column
    column_sum = df["AC_PWT_CS"].sum()
    
    # # Display the result in the Label widget
    result = subcslbl.config(text=column_sum)

# # Create the main window
# root = tk.Tk()
# root.title("Column Sum Data from Excel")

# # Create an Entry widget to input the column name
# column_entry = ttk.Entry(root, width=30)
# column_entry.grid(row=0, column=1, padx=10, pady=10)

# # Create a Label to prompt for the column name
# column_label = ttk.Label(root, text="Column Name:")
# column_label.grid(row=0, column=0, padx=10, pady=10)

# # Create a Label to display the result
# label_result = ttk.Label(root, text="Sum will appear here", width=50, anchor="w", justify="left")
# label_result.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# # Create a button to load data from Excel and calculate the column sum
# load_button = ttk.Button(root, text="Load and Sum Column", command=load_and_sum_column)
# load_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the application
################################# Summery ##################################################
def summery(root):
    summryframe = tk.LabelFrame(root,text='SUMMERY',font=('New Times Roman',10,'bold'),
                fg='blue',padx=10,relief=GROOVE,border=5)

    suburbanframe = tk.LabelFrame(summryframe,text='Suburban',font=('New Times Roman',10,'bold'),
                fg='blue',padx=10,relief=GROOVE,border=5)

    tk.Label(suburbanframe,text='Total C/S',font=('New Times Roman',12,'bold')).grid(row=0,column=0)

    subcslbl=IntVar()
    subcslbl= tk.Label(suburbanframe,text='',font=('New Times Roman',12,'bold'),
                    relief=GROOVE,padx=10,pady=5,bd=3,width=10)
    subcslbl.grid(row=0,column=1)

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
    
    load_and_sum_column()

