import tkinter as tk


win = tk.Tk()
win.title("Staion PCDO")
width= win.winfo_screenwidth()               
height= win.winfo_screenheight()               
win.geometry("%dx%d" % (width, height))
win.config(bg='Cadetblue1')

win.mainloop()