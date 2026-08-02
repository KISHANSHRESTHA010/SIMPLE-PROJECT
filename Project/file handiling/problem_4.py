#  A program to append a line to a file 

file_name=input("Enter name of file:")
line_add=input("Enter line to be added:")

try:
    with open(file_name,"a") as file:
        file.write(line_add +'\n')
except Exception as e:
    print("An error occured",e)

print("Data appended successfully")