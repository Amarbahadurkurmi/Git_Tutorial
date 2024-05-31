import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import filedialog,messagebox
import menu

def export():
    # Ask the user for the save location and file name
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if file_path:
        # Save the DataFrame to a CSV file
        df.to_excel(file_path, index=False)
        print(f"Data exported to {file_path}")
        messagebox.showinfo('Success','Data Save Successfully')

# Read the Excel file
df = pd.read_excel('stnpcdo.xlsx')

# Get column headers
columns = df.columns.tolist()

# Create the main application window
root = tk.Tk()
root.title("Treeview from Excel")
width= root.winfo_screenwidth()               
height= root.winfo_screenheight()               
root.geometry("%dx%d" % (width, height))

menu.menub(root=root,tk=tk)
# Create a frame for the Treeview and Scrollbars
frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True)

# Create the Treeview widget
tree = ttk.Treeview(frame, columns=columns, show='headings')

# Format columns
for col in columns:
    tree.column(col, anchor=tk.W, width=120)
    tree.heading(col, text=col, anchor=tk.W)

# Create vertical scrollbar
vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
vsb.pack(side='right', fill='y')

# Create horizontal scrollbar
hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
hsb.pack(side='bottom', fill='x')

# Configure the Treeview to use the scrollbars
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Insert data into Treeview
for index, row in df.iterrows():
    tree.insert('', 'end', values=row.tolist())

# Pack the Treeview widget
tree.pack(fill=tk.BOTH, expand=True)

# Create an export button
export_button = tk.Button(frame, text="Export to Excel", command=export)

export_button.pack(pady=10)

# Run the application
root.mainloop()
