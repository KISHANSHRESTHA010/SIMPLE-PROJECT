# A programme that returns true if the sting is a valild email
import re

def test(n):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern,n):
        print("Valid email")
        return True
    
email=input("Enter email:")
test(email)