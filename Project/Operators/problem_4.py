"""
Is and == are both conditional operators but they check different things

1.is = is check  the object is in same memory(same object)

2.'==' = "==" checks the value (same value)
"""

# example
a=1000
b=1000

print(a==b) #True because both have same value
print(a is b) #False because of different object