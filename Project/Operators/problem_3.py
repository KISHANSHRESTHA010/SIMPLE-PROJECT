# A programme that checks if the number is between 10 and 100

number=float(input("Enter number:"))

if number>10 and number<100: #Uses logical opearator (and) and (<>) to check if number satisfies condition
    print(f"{number} is between 10 and 100")

else:
    print(f"{number} isn't between 10 and 100")