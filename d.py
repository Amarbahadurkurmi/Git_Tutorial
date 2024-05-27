import openpyxl
import tkinter as tk
from tkinter import ttk, messagebox

# Function to load data from Excel and calculate sum
def load_and_sum_data():
    try:
        workbook = openpyxl.load_workbook('stnpcdo.xlsx')
    except FileNotFoundError:
        messagebox.showerror("Error", "The file 'stnpcdo.xlsx' was not found.")
        return

    sheet = workbook.active

    sum_value = 0
    for row in sheet.iter_rows(min_row=2, values_only=True):
        for cell in row:
            if isinstance(cell, (int, float)):  # Ensure the cell contains a number
                sum_value += cell

    label_result.config(text=f"Sum: {sum_value}")

# Create the main window
root = tk.Tk()
root.title("Sum Data from Excel")

# Create a Label to display the result
label_result = tk.Label(root, text="Sum will appear here", width=50)
label_result.grid(row=0, column=0, padx=10, pady=10)

# Create a button to load data from Excel and calculate the sum
load_button = ttk.Button(root, text="Load and Sum Data", command=load_and_sum_data)
load_button.grid(row=1, column=0, padx=10, pady=10)

# Run the application
root.mainloop()
