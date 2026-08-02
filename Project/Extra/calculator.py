# # using input
# # a and b are integers but output can be floats too.
# a = int(input("Enter first_number:" ))
# b = int(input("Enter second_number: "))
# ans1 = a + b
# print("addition of ",a,"and ",b,"is ",ans1)
# ans2 = a - b
# print("subtraction of ",a,"and ",b,"is",ans2)
# ans3 = a * b
# print("multiplication of ",a,"and ",b,"is ",ans3)
# ans4 = a / b
# print("division of ",a,"and ",b,"is ",ans4)

# # without using input
# a = 1
# b = 2
# print("the sum of ",a,"+",b,"is: ",a + b )
# print("the differece of ",a,"-",b,"is: ",a - b )
# print("the multiplication of ",a,"*",b,"is: ",a * b )
# print("the division of ",a,"/",b,"is: ",a / b )


# def add(x,y):
#     return x+y

# def sub(x,y):
#     return x-y
# def product(x,y):
#     return x*y
# def div(x,y):
#     if y==0:
#         raise Exception("Y can't be 0")
#     else:
#         return x/y
    
# while True:
#     print("\n----------------Calculator------------------")
#     print("Choices")
#     print("1.Add/Sum")
#     print("2.Subtracat")
#     print("3.Multiply")
#     print("4.Divide")
#     print("5.Exit")

#     choice=int(input("Enter a choice 1/2/3/4/5/: "))

#     if choice==5:
#         print("Exiting calculator")
#         break

#     if choice in [1,2,3,4]:
#         x=first_number=float(input("Enter first number: "))
#         y=second_number=float(input("Enter second number: "))

#         if choice==1:
#             print(f"RESULT:{(x,y)}")
#         elif choice==2:
#             print(f"RESULT:{add(x,y)}")
#         elif choice==2:
#             print(f"RESULT:{sub(x,y)}")
#         elif choice==3:
#             print(f"RESULT:{product(x,y)}")
#         elif choice==2:
#             print(f"RESULT:{div(x,y)}")
#     else:
#         print("Invalid operation")



import tkinter as tk

root=tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.resizable(True,True)

calculation=""
Entry_text=tk.StringVar()

entry=tk.Entry(root,textvariable=Entry_text,font=('Arial',20),width=32)
entry.grid(row=0,column=0,columnspan=5,padx=10,pady=50)

def add_calculation(char):
    global calculation
    calculation+=str(char)
    Entry_text.set(calculation)

def clear():
    global calculation
    calculation=""
    Entry_text.set("")

def delete():
    global calculation
    calculation=calculation[:-1]

def evaluate():
    global calculation
    try:
        result=str(eval(calculation))
        Entry_text.set(result)
        calculation=result
    except Exception as e:
        Entry_text.set=("Error")
        calculation=""

buttons=[
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("3",3,0),("2",3,1),("1",3,2),("+",3,3),
    (".",4,0),("0",4,1),("-",4,2),("=",4,3),
]
for (text,row,col) in buttons:
    if text=="=":
        action=evaluate
    else:
        action=lambda x=text: add_calculation(x)
    tk.Button(root,text=text,font=("Arial",18),command=action).grid(row=row,column=col,padx=0,pady=0,sticky="nsew")
    
tk.Button(root,text="C",font=("Arial",18),command=clear).grid(row=5,column=1,padx=0,pady=0,sticky="nsew")
tk.Button(root,text="del",font=("Arial",18),command=delete).grid(row=5,column=2,padx=0,pady=0,sticky="nsew")



root.mainloop()

