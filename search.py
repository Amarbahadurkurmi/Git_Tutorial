import pandas as pd
import tkinter as tk
from tkinter import ttk

# Function to load data from Excel and display in widgets
def load_data():
    # Read data from Excel file
    df = pd.read_excel('STN_PCDO.xlsx')  # Replace 'data.xlsx' with your Excel file name
    
    # Get the first row of data
    first_row = df.iloc[0]
    
    # Display data in Entry and Label widgets
    entry1.delete(0, tk.END)
    entry1.insert(0, first_row[0])
    
    entry2.delete(0, tk.END)
    entry2.insert(0, first_row[1])
    
    label1.config(text=first_row[2])

# Create the main window
root = tk.Tk()
root.title("Excel Data Display")

# Create Entry widgets
entry1 = tk.Entry(root, width=30)
entry1.grid(row=0, column=1, padx=10, pady=10)

entry2 = tk.Entry(root, width=30)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create Label widgets
label1 = tk.Label(root, text="", width=30)
label1.grid(row=2, column=1, padx=10, pady=10)

# Create static labels for the Entry widgets
tk.Label(root, text="Column 1:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Column 2:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Column 3:").grid(row=2, column=0, padx=10, pady=10)

# Create a button to load data from Excel
load_button = ttk.Button(root, text="Load Data", command=load_data)
load_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
