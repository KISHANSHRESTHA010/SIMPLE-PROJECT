# A programme that makes a random password

import random
import string

def gen_password(length):

    if length<8:
        print("Password must be atleast 8 characters long")
        length=8

    character=string.ascii_uppercase+string.ascii_lowercase+string.punctuation+string.digits

    password=[
                random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.punctuation),
                random.choice(string.digits)
        ]#Makes the ranges of characters which can be choosen
    
    remaining_len=length-len(password)
    password+=random.choices(character,k=remaining_len)

    random.shuffle(password)
    return ''.join(password)    

print("----------Password generator------------")
length=int(input("Enter desired length of password:"))
result=gen_password(length)
print(f"Password:{result}")

