# A programmme of a cli calculator

# for making operation
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

# Main loop
def main():
    print("--------------Calculator-------------------")
    while True:
        print("Operations")
        print("-"*20)
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exit")
        print("-"*20)

        choice=int(input("Enter your choice(1/2/3/4/5):"))
        if choice==5:
            print("Thanks for visiting")
            break

        if choice not in [1,2,3,4,5]:
            print("Invalid choice")
            continue

        try:
            num_1=float(input("Enter first number:"))
            num_2=float(input("Enter second number:"))
        except ValueError:
            print("Use valid number")

        if choice==1:
            result=add(num_1,num_2)
        elif choice==2:
            result=subtract(num_1,num_2)
        elif choice==3:
            result=multiply(num_1,num_2)
        else:
            result=divide(num_1,num_2)

        
        print(f"Result:{result}")
        print("-"*20)

if __name__=="__main__":
    main()