# A programme that calculates between days between date

from datetime import datetime

date1=input("Enter first date(YYYY-MM-DD):")
date2=input("Enter second date(YYYY-MM-DD):")


try:
    date1=datetime.strptime(date1,"%Y-%m-%d")
    date2=datetime.strptime(date2,"%Y-%m-%d")
except ValueError:
    print("Invalid date")

if date2<date1:
    print("Please enter grater date first")

difference=abs((date1-date2).days)
print(f"Days:{difference}")