# A program to read a text file

file_name=input("Enter the name of text file(with .txt extention):")
try:
    with open(file_name,"r") as file:
        content=file.read()
        print("\n File content")
        print(content)
except FileNotFoundError:
    print("File not found")