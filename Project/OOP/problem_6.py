class student:
    def __init__(self,name,age,marks,):
        self.name=name
        self.age=age
        self.marks=marks
        self.grade=self.calculate_grade()

    def calculate_grade(self):
        percent=self.marks/5

        if percent>=90:
            return "A+"
        elif percent>=80:
            return "A"
        elif percent>=70:
            return "B+"
        elif percent>=60:
            return "B"
        elif percent>=50:
            return "C+"
        elif percent<=40:
            return "C"
        else:
            return "F"

    def show(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Total marks:{self.marks}")
        print(f"Grade:{self.grade}")

student1=student("Kishan",16,400)
student1.show()