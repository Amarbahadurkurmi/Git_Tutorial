import pandas as pd
import tkinter as tk
from tkinter import messagebox

def stn_nr():
    # Load the Excel file
    df = pd.read_excel('stnpcdo.xlsx')

        # Access the first column (assuming the first column is named 'A' or you know its name)
    enter_stn_list = df.iloc[:,0].tolist()

        # Iterate through the values in the first column
    # for value in enter_stn_list:
    #     print(value)
        
        # Load the Excel file
    df = pd.read_excel('stnlist.xlsx')
        
        # Access the first column (assuming the first column is named 'A' or you know its name)
    stnlist = df.iloc[:,0].tolist()

    # for value in stnlist:
    #     print(value)
        
    updatelist = stnlist

    for i in enter_stn_list:
        for j in stnlist:
            if i == j:
                updatelist.remove(i)
    
    messagebox.showinfo("Success",updatelist)
    # print(updatelist)



