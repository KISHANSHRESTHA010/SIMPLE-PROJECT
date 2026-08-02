# a programme that checks if a number is prime

num=int(input("Enter number: "))

if num<=1:
    print(f"{num} isn't a prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is composite")
            break
    else:
        print(f"{num} is prime")