import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def load_excel_and_sum_column():
    # Prompt the user to select an Excel file
    # file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    # if not file_path:
    #     return

    # Load the Excel file into a DataFrame
    df = pd.read_excel('stnpcdo.xlsx')

    # Prompt the user to input the column name
    column_name = column_entry.get()
    if column_name not in df.columns:
        messagebox.showerror("Error", f"Column '{column_name}' not found in the Excel sheet.")
        return

    # Calculate the sum of the specified column
    column_sum = df[column_name].sum()

    # Update the label to display the result
    result_label.config(text=f"Sum of '{column_name}': {column_sum}")

# Create the main application window
root = tk.Tk()
root.title("Excel Column Sum Calculator")

# Create and place widgets
tk.Label(root, text="Select an Excel file and enter the column name:").pack(pady=10)

tk.Button(root, text="Select Excel File", command=load_excel_and_sum_column).pack(pady=5)

tk.Label(root, text="Column Name:").pack(pady=5)
column_entry = tk.Entry(root)
column_entry.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

# Run the application
root.mainloop()
