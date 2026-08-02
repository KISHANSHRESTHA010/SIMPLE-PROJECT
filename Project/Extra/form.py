import tkinter as tk
import sqlite3
from tkinter import messagebox

# To make a empty form
root=tk.Tk()
root.geometry("300x300")
root.resizable(False,False)
root.title("FORM")


# to CONNECT DATA to sqlite3
conn=sqlite3.connect("data base/students.sqlite3")
c=conn.cursor()
def table():
    sql="""
        CREATE TABLE IF NOT EXISTS STUDENTS(
        id INTEGER PRIMARY KEY,
        NAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL UNIQUE,
        ADDRESS TEXT       
        )
    """
    conn.commit()

def insert_table(name,email,address):
    name=name_entry.get()
    email=email_entry.get()
    address=address_entry.get()
    sql="""
        INSERT INTO STUDENTS(NAME,EMAIL,ADDRESS)
        VALUES(?,?,?)
    """
    c.execute(sql(name,email,address))
    conn.commit()

def update(name,email,address):
    name=name_entry.get()
    email=email_entry.get()
    address=address_entry.get()

    sql="""
        UPDATE STUDENTS SET name=?,email=?,address=?WHERE id=?
    """
    c.execute(sql(name,email,address,id))
    conn.commit()
    messagebox.showinfo(root,text="Data updated successfully")

def delete(id):
    name=name_entry.get()
    email=email_entry.get()
    address=address_entry.get()
    sql="""
        DELETE FROM STUDENTS WHERE id=?
    """
    c.execute(sql(id))
    conn.commit()
    print("DATA DELETED SUCESSFULLY")

def select():
    sql="""
        SELECT * FROM STUDENTS
    """
    data=c.execute(sql)
    print(data.fetchall())

label1=tk.Label(root,text="Student id").pack()
id_entry=tk.Entry(root)
id_entry.pack(pady=5)

label2=tk.Label(root,text="Name").pack()
name_entry=tk.Entry(root)
name_entry.pack(pady=5)

label3=tk.Label(root,text="Email").pack()
email_entry=tk.Entry(root)
email_entry.pack(pady=5)

label4=tk.Label(root,text="Address").pack()
address_entry= tk.Entry(root)
address_entry.pack(pady=5)


root.mainloop()