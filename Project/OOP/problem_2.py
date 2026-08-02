class Bankaccount:
    def __init__(self,username,balance=0):
        self.username=username
        self.balance=balance

    def deposit(self,amount):
        if amount<=0:
            print("Deposit amount must be positive")
        else:
            self.balance+=amount
            print(f"Rs{amount} deposited sucessfuly.Your new balance is Rs{self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print(f"Insufficient Balance.Your balance is Rs{self.balance}")
        elif amount<=0:
            print("Amount must be positive")
        else:
            print(f"You withdrew Rs{amount} from your account")

my_account=Bankaccount("Kishan")
my_account.deposit(5000)
my_account.withdraw(5000)