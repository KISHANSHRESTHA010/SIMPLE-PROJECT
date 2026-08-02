# A programme that breaks when number 5 is entered

while True:
    num=int(input("Enter number:"))

    if num==5:
        print("Exiting")
        break
    else:
        print(f"You wrote:{num}")