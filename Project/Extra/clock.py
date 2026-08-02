import tkinter as tk
from time import strftime

# To make a gui application
root=tk.Tk()
root.title("Clock")

def time():
    current_time=strftime("%H:%M:%S %p")
    label.config(text=current_time)
    label.after(1000,time)

label=tk.Label(root,font=("Arial",60),fg="cyan",background="black")
label.pack(anchor="center")

time()
root.mainloop()
