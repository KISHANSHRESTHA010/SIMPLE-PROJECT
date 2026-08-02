# import random
# import string

# def generate_password(length):
#     if length<8:
#         print("Password must be atleast 8 characters long")
#         length=8

#     characater=string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits

#     password=[
#             random.choice(string.ascii_lowercase),
#             random.choice(string.ascii_uppercase),
#             random.choice(string.punctuation),
#             random.choice(string.digits)
#         ]

#     password+=random.choices(characater,k=length)
#     random.shuffle(password)
#     return ''.join(password)
    
# print("\n----------------Password generator--------------------")
# length=int(input("Enter your desired length(min 8):"))
# password=generate_password(length)
# print(f"Generate password: {password}")