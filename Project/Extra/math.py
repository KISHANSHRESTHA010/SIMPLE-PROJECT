import math

# A programme that finds area,circumference of circle
print("===================================WELCOME TO MATH.GPT=============================")
name = input("Enter your name: ")
radius = float(input("Enter radius(in cm): "))
CIRCUMFERENCE = 2*math.pi*radius
AREA = math.pi*pow(radius,2)
print("==================================RESULT=============================================")
print(f"User's Name:{name}")
print(f"Radius:{radius}cm")
print(f"CIRCUMFERENCE:{CIRCUMFERENCE}cm")
print(f"Area:{AREA}sq cm")
print("                              THANKS FOR VISITING                                     ")

