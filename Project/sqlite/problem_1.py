import sqlite3

conn=sqlite3.connect("sqlite/employee.sqlite3")
myc=conn.cursor()

def table():
    sql="""
    CREATE TABLE IF NOT EXISTS EMPLOYEE(
    NAME TEXT NOT NULL,
    SALARY INTEGER
    )
    """
    myc.execute(sql)

def insert_table(name,salary):
        sql="""
        INSERT INTO EMPLOYEE(NAME,SALARY)
        VALUES(?,?)
        """
        myc.execute(sql,(name,salary))
        conn.commit()
        print("Data inserted successfully")

table()
name=input("Enter name:")
salary=int(input("Enter salary:"))
insert_table(name,salary)
conn.close()