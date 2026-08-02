# A program to read a csv file

import csv

filename=input("Enter name of file:")

try:
    with open(filename,"r") as file:
        reader=csv.reader(file)

        print("         CSV content           ")
        print("-------------------------------")
        for row in reader:
            print(row)

except Exception as e:
    print("An error ocurred",e)


