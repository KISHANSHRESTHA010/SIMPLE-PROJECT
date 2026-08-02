print("============Student Result=============")
num =int(input("Enter number of students: "))
students_marks=[]
sid=1
while sid<=num:
    print(f"=========Student ID: {sid}===========")
    nep =int(input("Enter Nepali marks: "))
    eng =int(input("Enter English marks: "))
    math =int(input("Enter Math marks: "))
    sci =int(input("Enter Science marks: "))
    soc =int(input("Enter Social marks: "))
    total = nep + eng + math + sci + soc
    students_marks.append(total)
    sid+=1

print("Sid\t Total Mark \tPercentage\t Grade")
student_id=1
for total in students_marks:
    per=total/5
    grade=""
    if per>=90:
        grade="A+"
    elif per>=80:
        grade="A"
    elif per>=70:
        grade="B+"
    elif per>=60:
        grade="B"
    elif per>=50:
        grade="C+"
    elif per>=40:
        grade="C"
    else:
        grade="F"
    print(f"{student_id}\t {total} \t\t{per:.2f}\t\t{grade}")
    student_id+=1
