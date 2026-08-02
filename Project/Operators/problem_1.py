# a programme that checks if the number is even or odd

number=int(input("Enter number:"))

if number%2==0:  #Uses modulo(%) operator to check if the number is even
    print(f"{number} is Even")

else:
    print(f"{number} is Odd")