import math

# To find square root
num=int(input("Enter number:"))

sqroot=math.sqrt(num)
print(sqroot)

# To find sin
degree=float(input("Enter angle in degree:"))

radian=math.radians(degree)

sinvalue=math.sin(radian)

print(f"{degree}°={sinvalue}")

# To find log
number=float(input("Enter a number:"))

base=input("Enter a base(press enter for natural base):")
if base=="":
    logarithmn=math.log(number)
    print(f"{logarithmn:.2f}")
else:
    base=float(base)
    logarithmn=math.log(number,base)
    print(f"{logarithmn:.2f}")