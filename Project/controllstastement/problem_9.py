# A programme of a login system

email1="kishanshrestha936@gmail.com"
password1="98@#$"

attempts=3

while attempts>0:
    email2=input("Enter email:")
    if email2==email1:
        password2=input("Enter password:")
        if password2==password1:
            print("Log-in successful")
            break
        else:
            print("Invalid password")
    else:
        print("Invalid email")

    attempts-=1

if attempts==0:
    print("Account blocked")
