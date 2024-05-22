import tkinter as tk

def update_label(*args):
    try:
        # Get the current values from both entry widgets
        num1 = float(entry_var1.get() or 0)
        num2 = float(entry_var2.get() or 0)
        
        # Calculate the sum
        result = num1 + num2
        
        # Update the label with the result
        result_label.config(text=f"Result: {result}")
    except ValueError:
        # If there's a value error (e.g., input is not a number), just ignore it
        result_label.config(text="Invalid input")

def main():
    global entry_var1, entry_var2, result_label

    root = tk.Tk()
    root.title("Live Addition")

    # Create StringVar variables to hold the entry widget values
    entry_var1 = tk.StringVar()
    entry_var2 = tk.StringVar()

    # Trace changes to the StringVar variables
    entry_var1.trace_add("write", update_label)
    entry_var2.trace_add("write", update_label)

    # Create and place the first entry widget
    entry1 = tk.Entry(root, textvariable=entry_var1)
    entry1.pack(pady=5)

    # Create and place the second entry widget
    entry2 = tk.Entry(root, textvariable=entry_var2)
    entry2.pack(pady=5)

    # Create and place the label to display the result
    result_label = tk.Label(root, text="Result: 0")
    result_label.pack(pady=5)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
