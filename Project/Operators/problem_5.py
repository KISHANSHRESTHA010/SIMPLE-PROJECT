# A programmes that chooses largest number using comparision and conditional operator

a=first_num=float(input('Enter first number:'))
b=second_num=float(input('Enter second number:'))
c=third_num=float(input('Enter third number:'))

if a>b and a>c:
    print(f"{a} is the largest")
elif b>c and b>a:
    print(f"{b} is the largest")
else:
    print(f"{c} is the largest")


# OR
print(max(a,b,c))