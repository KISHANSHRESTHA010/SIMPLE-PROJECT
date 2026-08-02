students=[
    {'name':'ram','gender':'male','status':True},
    {'name':'sophia','gender':'female','status':False},
    {'name':'gopal','gender':'male','status':False},
    {'name':'hari','gender':'male','status':False},
    {'name':'sita','gender':'female','status':True},

]


users = 0
male = 0
female = 0
active = 0
inactive = 0
active_male = 0
active_female = 0
inactive_male = 0
inactive_female = 0

for student in students:
    users+=1
    if student["gender"]=="male":
        male+=1
        if student["status"]==True:
            active_male+=1
        else:
            inactive_male+=1
    else:
        female+=1
        if student["status"]==True:
            active_female+=1
        else:
            inactive_female+=1

    if student["status"]==True:
        active+=1
    else:
        inactive+=1

print(f'total user:{users}')
print(f'total male:{male}')
print(f'total female:{female}')
print(f'total active user:{active}')
print(f'total active male:{active_male}')
print(f'total active female:{active_female}')
print(f'total inactive male:{inactive_male}')
print(f'total inactive female:{inactive_female}')