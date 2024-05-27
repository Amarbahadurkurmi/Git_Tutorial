import tkinter as tk

def open_new_window():
    # Get the current geometry
    current_geometry = root.winfo_geometry()
    
    # Destroy the current window
    root.destroy()
    
    # Create a new root window
    new_root = tk.Tk()
    new_root.geometry(current_geometry)
    new_root.title("New Window")
    
    # Add widgets to the new window as needed
    label = tk.Label(new_root, text="This is a new window with the same geometry")
    label.pack(pady=20)
    
    new_root.mainloop()

# Create the initial window
root = tk.Tk()
root.geometry("400x300")  # Set initial geometry
root.title("Initial Window")

# Add a button to open the new window
button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(pady=20)

root.mainloop()
