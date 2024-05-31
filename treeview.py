import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import openpyxl
import os

def export_to_excel():
    # Ask the user for the save location and file name
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        # Save the DataFrame to a CSV file
        df.to_csv(file_path, index=False)
        print(f"Data exported to {file_path}")

# Function to export data to Excel
def export_data_to_excel(data, file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in data:
        sheet.append(row)
    workbook.save(file_path)

# Function to populate Treeview
def populate_treeview(tree, data):
    tree.delete(*tree.get_children())
    for row in data:
        tree.insert('', 'end', values=row)

# Function to open file dialog and load Excel
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
    if file_path:
        try:
            data = load_data_from_excel(file_path)
            populate_treeview(tree, data)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

# Function to save data to Excel
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[('Excel Files', '*.xlsx')])
    if file_path:
        try:
            data = []
            for child in tree.get_children():
                data.append(tree.item(child)['values'])
            export_data_to_excel(data, file_path)
            messagebox.showinfo("Success", "Data exported successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {e}")

# Create the main window
root = tk.Tk()
root.title("Excel Data Viewer")

# Create a frame for the Treeview
frame = ttk.Frame(root)
frame.pack(fill='both', expand=True)

# Create the Treeview
tree = ttk.Treeview(frame, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), show='headings', height=8)
tree.heading(1, text="Batch")
tree.heading(2, text="AC_P_CS")
tree.heading(3, text="AC_P_AMT")
tree.heading(1, text="AC_D_CS")
tree.heading(2, text="AC_D_AMT")
tree.heading(2, text="FC_P_CS")
tree.heading(3, text="FC_P_AMT")
tree.heading(1, text="FC_D_CS")
tree.heading(2, text="FC_D_AMT")
tree.heading(1, text="IIND_CS")
tree.heading(2, text="IIND_CS")
tree.heading(3, text="UBL_CS")
tree.heading(1, text="UBL_AMT")
tree.heading(2, text="STAFF")
tree.heading(3, text="WD")
tree.heading(1, text="TOTAL_CS")
tree.heading(2, text="TOTAL_AMT")
tree.heading(3, text="LITT_CS")
tree.heading(1, text="LITT_AMT")
tree.heading(2, text="SM_CS")
tree.heading(3, text="SM_AMT")
tree.heading(2, text="FC_P_CS")
tree.heading(3, text="FC_P_AMT")
tree.heading(1, text="FC_D_CS")
tree.heading(2, text="FC_D_AMT")
tree.pack(side='left', fill='both')

# Add a scrollbar to the Treeview
scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side='right', fill='y')

# Create buttons for loading and saving files
btn_frame = ttk.Frame(root)
btn_frame.pack(fill='x', expand=True)

load_btn = ttk.Button(btn_frame, text="Load Excel File", command=open_file)
load_btn.pack(side='left', padx=10, pady=10)

save_btn = ttk.Button(btn_frame, text="Save to Excel File", command=save_file)
save_btn.pack(side='right', padx=10, pady=10)

# Run the application
root.mainloop()
