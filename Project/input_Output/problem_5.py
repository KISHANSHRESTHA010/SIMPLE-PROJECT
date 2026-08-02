# A programme that represents integer into octal and hexa

num=int(input("Enter number:"))

octa=oct(num)
hexa=hex(num)

print(f"Octadecimal representation of {num} is {octa}")
print(f"Hexadecimal representation of {num} is {hexa}")