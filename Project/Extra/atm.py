# print("==========WELCOME TO ATM============")
# PIN = int(input("Enter your PIN: "))
# BALANCE = int(10000)
# if PIN==1234:
#     task = {
#        1:("Check Balance: "),
#        2:("Withdraw Money: "),
#     }
#     choice = int(input("Enter your task: "))
#     if choice==1:
#         print(f"Your balance is {BALANCE}")
#     else:
#         amount = int(input('Enter your amount:'))
#         if amount<=10000:
#             print("TASK COMPLETED")
#         else:
#             print("Insufficient Balance")
# else:
#     print("Invalid PIN")


# # A detail ATM
# print("-----------------------Welcome to ATM--------------------------------")
# balance=10000
# PIN=1234

# def balance_check():
#     print(f"Your balance is Rs{balance}")

# def deposit():
#     global balance
#     amount=float(input("Enter deposit amount:Rs"))
#     if amount>0:
#         balance+=amount
#         print(f"Rs{amount} was deposited successful")
#         print(f"Your new balance is Rs{balance}")
#     else:
#         print("Invalid amount")

# def withdraw():
#     global balance
#     amount=float(input("Enter withdraw amount:Rs"))
#     if amount>0:
#         balance-=amount
#         print(f"Rs{amount} was  withdrawn sucessfully")
#         print(f"Your new balance is Rs{balance}")
#     else:
#         print("Invalid amount")

# # MAin
# tries=3
# while tries>0:
#     pin=int(input("Enter your 4 digit pin:"))
#     if pin==PIN:
#         print("Log in successful")
#         break
#     else:
#         tries-=1
#         print("Incorrect pin")
# if tries==0:
#     print("You ran out of tries")
# else:

#     print("-"*50)
#     print("\nChoices")
#     print("1.BALANCE CHECK")
#     print("2.Deposit amount")
#     print("3.Withdraw amount")
#     print("4.Exit")
#     print("-"*50)
#     choice = int(input("Enter your option(1/2/3/4):"))

#     if choice==1:
#         print(f"Rs{balance}")
#     elif choice==2:
#         deposit()
#     elif choice==3:
#         withdraw()
#     elif choice==4:
#         print("Exiting ATM")
#     else:
#         print("Invalid choice")

#     print("=========================Thanks for visiting========================")
