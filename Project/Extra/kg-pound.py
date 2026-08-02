import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x250")
root.resizable(False,False)
root.title("Weight conveter")

def convert():
    try:
        weight=float(entry.get())
        if unit_var.get()=="Kg to lb".lower():
            result=weight*2.20
            result_label.config(text=f"{result:.2f}lb")
        else:
            result=weight*0.4536
            result_label.config(text=f"{result:.2f}kg")

    except Exception as e:
        messagebox.showwarning("Please enter valid number")

unit_var=tk.StringVar(value="Options") 
dropdown=tk.OptionMenu(root,unit_var,"kg to lb","lb to kg")
dropdown.pack(pady=10)

entry=tk.Entry()
entry.pack(pady=10)

btn=tk.Button(root,text="Convert",font=("Arial",15),command=convert)
btn.pack(pady=10)

result_label=tk.Label(root,text="RESULT",width=20)
result_label.pack(pady=10)

root.mainloop()


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("300x250")
# root.resizable(False, False)
# root.title("Weight Converter")

# def convert():
#     try:
#         weight = float(entry.get())
#         if unit_var.get() == "Kg to lb":                              
#             result = weight * 2.20462
#             result_label.config(text=f"{result:.2f} lb")
#         elif unit_var.get() == "lb to Kg":
#             result = weight * 0.453592
#             result_label.config(text=f"{result:.2f} kg")
#         else:
#             messagebox.showwarning("Selection Error", "Please choose a conversion type.")
#     except ValueError:
#         messagebox.showwarning("Input Error", "Please enter a valid number.")


# unit_var = tk.StringVar(value="Options")
# dropdown = tk.OptionMenu(root, unit_var, "Kg to lb", "lb to Kg")
# dropdown.pack(pady=10)

# entry = tk.Entry()
# entry.pack(pady=10)

# btn = tk.Button(root, text="Convert", font=("Arial", 15), command=convert)
# btn.pack(pady=10)

# result_label = tk.Label(root, text="RESULT", width=20)
# result_label.pack(pady=10)

# root.mainloop()
