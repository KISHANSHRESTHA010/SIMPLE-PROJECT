# A programme that prints prime number between 1 and 50

def prime(n):
    if n<=1:
        return False
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
         return False
    
    return True
    
for num in range(1,51):
    if prime(num):
        print(num)
        