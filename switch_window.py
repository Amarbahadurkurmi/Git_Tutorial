import tkinter as tk

def open_new_window():
    # Destroy the current window
    root.destroy()
    
    # Create a new window
    new_window = tk.Tk()
    new_window.title("New Window")
    
    label = tk.Label(new_window, text="This is the new window!")
    label.pack(pady=20)
    
    button = tk.Button(new_window, text="Close", command=new_window.destroy)
    button.pack(pady=10)
    
    new_window.mainloop()

# Create the initial window
root = tk.Tk()
root.title("Initial Window")

label = tk.Label(root, text="This is the initial window!")
label.pack(pady=20)

button = tk.Button(root, text="Open New Window", command=open_new_window)
button.pack(pady=10)

root.mainloop()
