import random

choice=random.randint(1,101)
guess=None

while guess!=choice:
    guess=int(input("Enter a number:"))

    if guess<choice:
        print("Higher")

    elif guess==choice:
        print("Correct")
        
    else:
        print("lower")