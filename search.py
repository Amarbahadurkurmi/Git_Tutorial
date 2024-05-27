import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load the Excel file
df = pd.read_excel('stnpcdo.xlsx')  # Make sure your file path is correct

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Excel Data Search")

        # Create a frame for the search options
        search_frame = tk.Frame(root)
        search_frame.pack(pady=10)

        # Dropdown menu for selecting column
        self.column_var = tk.StringVar()
        self.column_var.set(df.columns[1])
        column_menu = ttk.Combobox(search_frame, textvariable=self.column_var, values=list(df.columns))
        column_menu.pack(side=tk.LEFT, padx=5)

        # Entry for search value
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, padx=5)

        # Search button
        search_button = tk.Button(search_frame, text="Search", command=self.search)
        search_button.pack(side=tk.LEFT, padx=5)

        # Frame for displaying results
        self.result_frame = tk.Frame(root)
        self.result_frame.pack(pady=10)

    def search(self):
        # Clear previous results
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Get search parameters
        column_name = self.column_var.get()
        search_value = self.search_var.get()

        # Perform the search
        results = df[df[column_name].astype(str) == search_value]

        if results.empty:
            result_label = tk.Label(self.result_frame, text="No results found.")
            result_label.pack()
        else:
            # Display the results in entry fields
            for idx, row in results.iterrows():
                for col_name in df.columns:
                    frame = tk.Frame(self.result_frame)
                    frame.pack(fill=tk.X, pady=2)

                    label = tk.Label(frame, text=col_name, width=20, anchor='w')
                    label.pack(side=tk.LEFT)

                    entry = tk.Entry(frame, width=50)
                    entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
                    entry.insert(0, str(row[col_name]))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
