# A programme that prints multipliscation of a number

num=int(input("Enter a number:"))
print(f"\nMiltiplication table of {num}")
for i in range(1,11):
    print(f"{num}*{i}={num*i}")