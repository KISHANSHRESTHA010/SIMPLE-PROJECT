
def add(x,y):
    return x+y

def sub(x,y):
    return x-y
def product(x,y):
    return x*y
def div(x,y):
    if y==0:
        raise Exception("Y can't be 0")
    else:
        return x/y
    
while True:
    print("\n----------------Calculator------------------")
    print("Choices")
    print("1.Add/Sum")
    print("2.Subtracat")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")

    choice=int(input("Enter a choice 1/2/3/4/5/: "))

    if choice==5:
        print("Exiting calculator")
        break

    if choice in [1,2,3,4]:
        x=first_number=float(input("Enter first number: "))
        y=second_number=float(input("Enter second number: "))

        if choice==1:
            print(f"RESULT:{(x,y)}")
        elif choice==2:
            print(f"RESULT:{add(x,y)}")
        elif choice==2:
            print(f"RESULT:{sub(x,y)}")
        elif choice==3:
            print(f"RESULT:{product(x,y)}")
        elif choice==2:
            print(f"RESULT:{div(x,y)}")
    else:
        print("Invalid operation")