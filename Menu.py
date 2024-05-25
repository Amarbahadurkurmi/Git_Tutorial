import tkinter as tk
from tkinter import messagebox
def menub(root):
    def new_file():
        messagebox.showinfo("Info", "New File Selected")

    def open_file():
        messagebox.showinfo("Info", "Open File Selected")

    def save_file():
        messagebox.showinfo("Info", "Save File Selected")

    def exit_app():
        root.quit()



    # Create the menu bar
    menu_bar = tk.Menu(root)

    # Create the File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_app)

    # Add the File menu to the menu bar
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Attach the menu bar to the root window
    root.config(menu=menu_bar)

    # Run the application
    
