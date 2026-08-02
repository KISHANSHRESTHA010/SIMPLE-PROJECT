import tkinter as tk
from datetime import datetime

def calculate():
    try:
        birth_year=int(entry.get())
        current_year=datetime.now().year
        if birth_year>current_year:
            result_label.config(text="INVALID YEAR")
        elif birth_year<1900:
            result_label.config(text="Enter realistic year")
        else:
            age=current_year-birth_year
            result_label.config(text=f"You're {age} years old")

        
    except ValueError:
        result_label.config(text="ENTER VALID YEAR")

# TO make a tkinter gui application
root=tk.Tk()
root.geometry("200x150")
root.resizable(False,False)
root.title("Age Calculator")

# to get age
Label=tk.Label(root,text="Enter your birth year").pack()
entry=tk.Entry(root)
entry.pack(pady=5)

# button
btn=tk.Button(root,text="CALCULATE",font=("Arial",10),command=calculate)
btn.pack(pady=5)

# to get result
result_label=tk.Label(root,text="RESULT HERE",font=("ARIAL",10),fg="blue")
result_label.pack(pady=5)

root.mainloop()