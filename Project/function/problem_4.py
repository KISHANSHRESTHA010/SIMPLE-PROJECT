# A programme that takes a list and returns max and min

def add():

    num_element=int(input("Enter number of elements:"))
    number=[]

    for i in range(1,num_element+1):
        num=int(input("Enter number:"))
        number.append(num)

    return number

list=add()
maximun=max(list)
minium=min(list)

print(f"Max:{maximun}")
print(f"Min:{minium}")


