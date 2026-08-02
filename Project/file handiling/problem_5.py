# A program to take a user input and read it's content

file_name=input("Enter name of file:")

try:
    with open(file_name,"r") as file:
        content=file.read()

        print(content)
except Exception as e:
    print("An error occured",e)