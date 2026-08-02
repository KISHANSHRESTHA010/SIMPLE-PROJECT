import math 
import statistics

"""String"""
def is_plaindrome(s):
    """Checks if the string is plaindrome"""
    s=s.lower().replace(" "," ")
    return s==s[::-1]

def count_vowel(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

def reverse(s):
    return s[::-1]

"""Math"""

def factorial(n):
    """Outputs factorial of a number"""
    if n<0:
        raise ValueError("Enter valid number")
    return math.factorial(n)

def is_prime(n):
    if n<=1:
        raise ValueError("Enter valid value(>1)")
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if i%2==0:
                return False
        return True
    
def gcd(a,b):
    return math.gcd(a,b)

"""List"""
def remove_duplicates(list):
    seen=set()
    return [x for x in list if not(x in seen or seen.add(x))]

def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]

def average(list):
    if not list:
        return 0
    return statistics.mean(list)
