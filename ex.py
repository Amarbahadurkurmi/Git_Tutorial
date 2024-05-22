import tkinter as tk
from datetime import datetime

def update_time():
    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Update the label with the current date and time
    time_label.config(text=current_time)
    
    # Schedule the update_time function to be called again after 1000 milliseconds (1 second)
    root.after(1000, update_time)

def main():
    global time_label, root

    root = tk.Tk()
    root.title("Date and Time Display")

    # Create a label to display the current date and time
    time_label = tk.Label(root, font=("Arial", 20))
    time_label.pack(pady=20)

    # Initialize the time update
    update_time()

    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
