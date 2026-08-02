import sqlite3

conn=sqlite3.connect("sqlite/employees.sqlite3")
myc=conn.cursor()

def table():
    sql="""
    CREATE TABLE IF NOT EXISTS EMPLOYEEs(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    SALARY INTEGER
    )
    """
    myc.execute(sql)

def insert_table(name,salary):
        sql="""
        INSERT INTO EMPLOYEES(NAME,SALARY)
        VALUES(?,?)
        """
        myc.execute(sql,(name,salary))
        conn.commit()
        print("Data inserted successfully")

def update(ID,name,salary):
    myc.execute("UPDATE EMPLOYEES SET name=?,salary=?WHERE ID=?",(name,salary,ID))
    conn.commit()
    if myc.rowcount:
        print("Data updated successfully.")
    else:
         print("Employee ID  not found.")

def delete(ID):
    myc.execute("DELETE FROM EMPLOYEES WHERE ID=?",(ID,))
    conn.commit()
    if myc.rowcount:
        print("Data deleted successfully")
    else:
        print("Employee id not found")

def show_data():
    myc.execute("SELECT * FROM EMPLOYEES")
    rows=myc.fetchall()
    print("Employee Records:")
    if rows:
        for row in rows:
            print(f"ID:{row[0]}.Name:{row[1]},Salary:{row[2]}")
    else:
        print("No records available")
         

def main():
    table()
    while True:
        print('\n--------Options--------------')
        print("1.Insert data")
        print("2.Update data")
        print("3.Delete data")
        print("4.Show data")
        print("5.Exit")

        choice=int(input("Enter your choice(1-5):"))

        if choice==1:       
            name=input("Enter name:")
            salary=int(input("Enter salary:"))
            insert_table(name,salary)
        elif choice==2:
            ID=int(input("Enter employee's id:"))
            name=input("Enter new name:")
            salary=int(input("Enter new salary:"))
            update(ID,name,salary)
        elif choice == 3:
                emp_id = int(input("Enter employee ID to delete: "))
                delete(emp_id)
        elif choice == 4:
                show_data()
        elif choice == 5:
                print("Exiting program.")
                break
        else:
            print("Invalid choice. Please enter 1-5.")

    conn.close()

main()      
