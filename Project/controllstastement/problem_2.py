# A programme that prints the fabonacii number

num=int(input("Enter how many fabinacci number you want:"))

# Initialize first two variables
a,b=0,1
count=0

# Main loop
while count<num:
    print(a,end=" ")

    # Generate another number 
    a,b=b,a+b
    count+=1

