# A program to copy file content

source=input("Enter name of source file:")
destination=input("Enter name of destination file:")
try:
    with open(source,"r") as src:
        content=src.read()

    with open(destination,"w") as dest:
        copy=dest.write(content)
    print("Data copied successfully")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("An error occured",e)
