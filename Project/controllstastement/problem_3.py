# A programme that calculates factorial

num=int(input("Enter number:"))
factorial=1
if num<0:
    print("Factorial can't be defined")
else:
    for i in range(1,num+1):
        factorial*=i #To calculate factorial
    
print(f"{num}!={factorial}")