import tkinter as tk
from tkinter import messagebox
import stn_not_received_prd

def menub(root,tk):
    
    def pcdo_window():
        root.destroy()
        import pcdo

    def mcdo_window():
        root.destroy()
        import mcdo

    def pcdo_view():
        root.destroy()
        import pcdo_list
    def mcdo_view():
        root.destroy()
        import mcdo_list
    
    def about_us():
        messagebox.showinfo("Info", "Save File Selected")

    def exit_app():
        root.quit()



    # Create the menu bar
    menu_bar = tk.Menu(root)

    # Create the File menu
    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="PCDO", command=pcdo_window)
    file_menu.add_command(label="MCDO", command=mcdo_window)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_app)

    data_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Data", menu=data_menu)
    data_menu.add_command(label="STN NR", command=stn_not_received_prd.stn_nr)
    data_menu.add_command(label="Batch NR", command=stn_not_received_prd.batch_nr)
    
    view_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="PCDO List", command=pcdo_view)
    view_menu.add_command(label="MCDO List", command=mcdo_view)
    # Add the File menu to the menu bar
    
    help_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About", command=about_us)
    
    

    # Attach the menu bar to the root window
    root.config(menu=menu_bar)

    # Run the application
    
