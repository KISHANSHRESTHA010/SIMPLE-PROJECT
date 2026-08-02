# A programmme that returns the factorial of a number 

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)#Recursive call
    
num=int(input("Enter your number:"))#To take user input
print("Factorial:",factorial(num))


