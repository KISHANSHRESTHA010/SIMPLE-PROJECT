# A programme that checks if the number is plaindrome

number=int(input("Enter number:"))

reverse=int(str(number)[::-1])

if number==reverse:
    print(f"{number} is a plaindrome number")

else:
    print(f"{number} isn't plaindrome number")