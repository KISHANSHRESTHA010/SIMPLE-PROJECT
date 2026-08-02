# import tkinter as tk
# from tkinter import messagebox

# def detail():
#     user_name=entry1.get()
#     password=entry2.get()

#     if not user_name or not password:
#         messagebox.showwarning("ENTER ALL DETAIL")
#     if user_name=="John":
#         password=entry2.get()
#         if password=="1234":
#             print("\n INFO")
#             print(f"Name:{user_name}")
#             print(f"PASSWORD:{password}")
#             messagebox.showinfo("DETAIL SUBMITTED")
#         else:
#             messagebox.showwarning("INVALID PASSWORD")
#     else:
#         messagebox.showwarning("INVALID USERNAME")
    

# root=tk.Tk()
# root.resizable(False,False)
# root.geometry("300x300")
# root.title("Log in")

# label1=tk.Label(root,text="ENTER NAME",width=20)
# label1.pack(pady=5)
# entry1=tk.Entry(root)
# entry1.pack(pady=10)

# label2=tk.Label(root,text="ENTER PASSWORD",width=20)
# label2.pack(pady=5)
# entry2=tk.Entry(root)
# entry2.pack(pady=10)

# btn=tk.Button(root,text="Sign in",font=("Arial",15),command=detail)
# btn.pack()

# root.mainloop()