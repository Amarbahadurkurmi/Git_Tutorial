import tkinter as tk
from tkinter import ttk
import pandas as pd

# Function to load Excel data
def load_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Function to search for a value in the second column and display the data
def search_data():
    search_value = search_entry.get()
    matching_row = df[df.iloc[:, 1] == search_value]
    
    if not matching_row.empty:
        for i, column in enumerate(df.columns):
            entry_widgets[i].delete(0, tk.END)
            entry_widgets[i].insert(0, str(matching_row.iloc[0, i]))
    else:
        for entry in entry_widgets:
            entry.delete(0, tk.END)
        result_label.config(text="No matching data found.")

# Load the Excel file
file_path = "stnpcdo.xlsx"  # Replace with your Excel file path
df = load_excel(file_path)

# Create the Tkinter window
root = tk.Tk()
root.title("Excel Data Search")

# Create a frame for the search bar
search_frame = ttk.Frame(root)
search_frame.pack(pady=10)

# Add a search label and entry
search_label = ttk.Label(search_frame, text="Search by Second Column:")
search_label.pack(side=tk.LEFT, padx=5)
search_entry = ttk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5)

# Add a search button
search_button = ttk.Button(search_frame, text="Search", command=search_data)
search_button.pack(side=tk.LEFT, padx=5)

# Create a frame for the entry widgets
entry_frame = ttk.Frame(root)
entry_frame.pack(pady=10)

# Create entry widgets for each column
entry_widgets = []
for column in df.columns:
    label = ttk.Label(entry_frame, text=column)
    label.pack(pady=5)
    entry = ttk.Entry(entry_frame, width=50)
    entry.pack(pady=5)
    entry_widgets.append(entry)

# Add a label for search results
result_label = ttk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
