#  A programme that checks gcd of two numbersd

def gcd(a,b):
    while b !=0:
        a,b=b,a%b
    return a 

number1=int(input('Enter first number:'))
number2=int(input("Enter second number:"))

print(f"GCD={gcd(number1,number2)}")