import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox

# Function to load data from Excel and calculate column-wise sum
def load_and_sum_data():
    try:
        # Load the Excel file
        df = pd.read_excel('stnpcdo.xlsx')
    except FileNotFoundError:
        messagebox.showerror("Error", "The file 'data.xlsx' was not found.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return

    # Calculate the sum for each column
    column_sums = df.sum(numeric_only=True)

    # Format the result as a string
    result_text = "\n".join([f"{col}: {total}" for col, total in column_sums.items()])

    # Display the result in the Label widget
    label_result.config(text=result_text)

# Create the main window
root = tk.Tk()
root.title("Column-wise Sum Data from Excel")

# Create a Label to display the result
label_result = tk.Label(root, text="Sums will appear here", width=50, anchor="w", justify="left")
label_result.grid(row=0, column=0, padx=10, pady=10)

# Create a button to load data from Excel and calculate the column-wise sums
load_button = ttk.Button(root, text="Load and Sum Data", command=load_and_sum_data)
load_button.grid(row=1, column=0, padx=10, pady=10)

# Run the application
root.mainloop()
