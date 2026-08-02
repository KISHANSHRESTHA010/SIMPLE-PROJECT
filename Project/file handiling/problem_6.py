# A program to store students record and retrive it

def add_students():
    name=input("Enter name of student:")
    age=int(input("Enter age of student:"))
    grade=int(input("Enter the class of student:"))

    with open("student.txt","a") as file:
        file.write(f"{name},{age},{grade}"+"\n")

    print("Data inserted successfullt")

def show_records():
    try:
        with open("student.txt","r") as file:
            content=file.read()
            file.close()

            print("Student's data")
            print(content)
    except Exception as e:
        print("An error occured",e)


def main():
    while True:
        print("---------Options-----------")
        print("1.Add student")
        print("2.Show records")
        print("3.Exit")

        choice=int(input("Enter choice(1/2/3):"))

        if choice==1:
            add_students()

        elif choice==2:
            show_records()
        
        elif choice==3:
            print("Thanks for visiting")
            break
        
        else:
            print("Inavlaid option")


if __name__=="__main__":
    main()