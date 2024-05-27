import tkinter as tk
from tkinter import Menu

def open_new_window():
    # Get the current geometry
    current_geometry = root.winfo_geometry()
    
    # Destroy the current window
    root.destroy()
    
    # Create a new root window
    new_root = tk.Tk()
    new_root.geometry(current_geometry)
    new_root.title("New Window")

    # Add menu to the new window
    menubar = Menu(new_root)
    new_root.config(menu=menubar)
    
    # Create a 'File' menu with a 'New' submenu
    file_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New", command=lambda: print("New File"))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=new_root.quit)
    
    # Create a 'Help' menu
    help_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=lambda: print("About"))

    # Add widgets to the new window as needed
    label = tk.Label(new_root, text="This is a new window with the same geometry")
    label.pack(pady=20)
    
    new_root.mainloop()

# Create the initial window
root = tk.Tk()
root.geometry("400x300")  # Set initial geometry
root.title("Initial Window")

# Add menu to the initial window
menubar = Menu(root)
root.config(menu=menubar)

# Create a 'File' menu with a 'New' submenu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: print("New File"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create a 'Help' menu
help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: print("About"))

# Add a button to open the new window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(pady=20)

root.mainloop()
