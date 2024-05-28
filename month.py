# # import tkinter as tk
# # from datetime import datetime

# # # Get the current month and year
# # now = datetime.now()
# # current_month_year = now.strftime("%B %Y")  # E.g., "May 2024"

# # # Create the main window
# # root = tk.Tk()
# # root.title("Current Month and Year")

# # # Create a label widget with the current month and year
# # label = tk.Label(root, text=current_month_year, font=("Arial", 20))

# # # Place the label in the window
# # label.pack(pady=20)

# # # Run the Tkinter event loop
# # root.mainloop()

# import tkinter as tk
# from datetime import datetime, timedelta

# def get_display_date():
#     today = datetime.today()
#     if today.day == 1:
#         # Move to the last day of the previous month
#         previous_month = today.replace(day=1) - timedelta(days=1)
#         display_date = previous_month.strftime("%B %Y")
#     else:
#         display_date = today.strftime("%B %Y")
#     return display_date

# # Create the main window
# root = tk.Tk()
# root.title("Current Month and Year")

# # Get the date to display
# display_date = get_display_date()

# # Create a label and add it to the window
# label = tk.Label(root, text=display_date, font=("Helvetica", 16))
# label.pack(pady=20)

# # Run the Tkinter event loop
# root.mainloop()
