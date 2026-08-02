"""
*args it provides you the flexibility of providing any value based on positional arguement
"""
def name(fname,lname):
    print(f"{fname} {lname}")

name("kishan","shrestha")

"""
**kwrgs provides the flexibilty of providing any value based on key arguements
"""

def name(fname,lname):
    print(f"{fname} {lname}")

name(lname="shrestha",fname="Kishan")
"""
Args don't provide flexibility to interchange the position of arguemants and value whereas **kwrgs provides flexibily to do so
"""