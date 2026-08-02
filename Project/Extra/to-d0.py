# # To add task
# todo_list=[]
# def add_task():
#     task=input("Enter a task: ")
#     todo_list.append(task)
#     print("Task added")

# # TO view task
# def view():
#     if not todo_list:
#         print("Empty list")
#     else:
#         print("\n------------To do list-------------------")
#         for i,task in enumerate(todo_list,start=1):
#             print(f"{i}.{task}")

# def delete_task():
#     view()
#     if todo_list:
#         try:
#             num_task=int(input("Enter the number of task: "))
#             if 1<=num_task<=len(todo_list):
#                 removed=todo_list.pop(num_task-1)
#                 print(f"Removed:{removed}")
#             else:
#                 print("Invalid task number")
#         except ValueError:
#             print("Please enter valid number")

# add_task()
# view()
# delete_task()


import tkinter as tk
from tkinter import messagebox
import sqlite3
import re

# TO CONNECT WITH DATABASE
conn=sqlite3.connect("data base/ToDo_list.sqlite3")
my_cursor=conn.cursor()

# To make a table
def table():
    sql="""
        CREATE TABLE IF NOT EXISTS TODO_LIST(
        id INTEGER PRIMARY KEY,
        TASK TEXT NOT NULL
        )
    """
    my_cursor.execute(sql)
    conn.commit()

table()

# To insert data in table
def insert_table():
    task=task_entry.get()
    pattern="^[A-Za-z ]+$"
    if task:
        if re.match(pattern,task):
            my_cursor.execute("INSERT INTO TODO_LIST(task)VALUES(?)",(task,))
            conn.commit()
            messagebox.showinfo("Successfull","TASK stored")
            clear()
        else:
            messagebox.showwarning("Inavlid task","Task must only contain alphabets")
    else:
        messagebox.showwarning("ERROR","TASK EMPTY")

# To update table
def update():
    try:
        id=int(id_entry.get())
    except ValueError:
        messagebox.showwarning("EEROR","Please enter valid ID(INTEGER)")
        return
    
    task=task_entry.get()

    if task:
        my_cursor.execute("UPDATE TODO_LIST SET TASK=? WHERE ID=?",(task,id))
        conn.commit()
        clear()
        messagebox.showinfo("DONE","TASK updated successfuly")
    else:
        messagebox.showwarning("ERROR","TASK EMPTY")
    
    clear()


# To delete task from table
def delete():
    try:
        id=int(id_entry.get())
    except ValueError:
        messagebox.showwarning("ERROR","ENTER VLAID ID")
        return
    
    my_cursor.execute("DELETE FROM TODO_LIST WHERE id=?",(id,))
    conn.commit()
    messagebox.showinfo("Success","TASK DELETED SUCCESSFULLY")
    clear()

# TO clear fields
def clear():
    id_entry.delete(0,tk.END)
    task_entry.delete(0,tk.END)

# TO VIEW TABLE
def select():
    my_cursor.execute("SELECT * FROM TODO_LIST")
    rows=my_cursor.fetchall()
    output="\n" .join([str(row)for row in rows])
    messagebox.showinfo("ALL TASK",output if output else "NO DATA FOUND")

# To make a gui application
root=tk.Tk()
root.title("TO-DO LIST")
root.geometry("300x300")
root.resizable(False,False)

# TO make id widget
label1=tk.Label(root,text="TEXT ID(Update/Delete)").pack()
id_entry=tk.Entry(root)
id_entry.pack(pady=5)

# TO make a task widget
label2=tk.Label(root,text="ENTER TASK").pack()
task_entry=tk.Entry(root)
task_entry.pack(pady=5)

# TO RUN INSERT CODE
btn1=tk.Button(root,text="INSERT DATA",font=("ARIAL",10),command=insert_table)
btn1.pack(pady=5)

# To run view
btn2=tk.Button(root,text="VIEW",font=("Arial",10),command=select)
btn2.pack(pady=5)

# To update
btn3=tk.Button(root,text="UPDATE",font=("ARIAl",10),command=update)
btn3.pack(pady=5)

# To dekete
btn4=tk.Button(root,text="DELETE",font=("ARIAL",10),command=delete)
btn4.pack(pady=5)

clear()
root.mainloop()