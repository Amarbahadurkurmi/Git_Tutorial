import tkinter as tk

def update_label(*args):
    try:
        # Get the current values from both entry widgets
        num1 = float(entry1.get() or 0)
        num2 = float(entry2.get() or 0)
        
        # Calculate the sum
        result = num1 + num2
        
        # Update the label with the result
        result_label.config(text=f"Result: {result}")
    except ValueError:
        # If there's a value error (e.g., input is not a number), just ignore it
        result_label.config(text="Invalid input")

def main():
    global entry1, entry2, result_label

    root = tk.Tk()
    root.title("Live Addition")

    # Create and place the first entry widget
    entry1 = tk.Entry(root)
    entry1.pack(pady=5)
    entry1.bind("<KeyRelease>", update_label)  # Bind key release event to update label

    # Create and place the second entry widget
    entry2 = tk.Entry(root)
    entry2.pack(pady=5)
    entry2.bind("<KeyRelease>", update_label)  # Bind key release event to update label

    # Create and place the label to display the result
    result_label = tk.Label(root, text="Result: 0")
    result_label.pack(pady=5)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
