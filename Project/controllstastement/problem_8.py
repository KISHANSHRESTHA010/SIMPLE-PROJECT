# A programme that makes result

# Takes user input
def add():
    student_name=input("Enter name:")

    english=float(input("Enter marks in English: "))
    nepali=float(input("Enter marks in Nepali:"))
    physics=float(input("Enter marks in Physics:"))
    maths=float(input("Enter marks in Maths: "))
    computer=float(input("Enter marks in Computer:"))

    total=english+nepali+physics+maths+computer

    return total,student_name

   

def calculate(total):
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

    return per,grade

def main(student_name,total,per,grade):
    print("\tStudent Name \t Total \t Percent(%) \t Grade")
    print(f"\t{student_name}\t{total}\t{per:2f}\t{grade}")

total,student_name=add()
per,grade=calculate(total)
main(student_name,total,per,grade)

