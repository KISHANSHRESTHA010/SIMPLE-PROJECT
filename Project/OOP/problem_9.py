class student:
    def __init__(self,name,age,marks):
        self.name=name
        self._age=age
        self.__marks=marks

    def get_marks(self):
        return self.__marks
    
    def get_age(self):
        return self._age
    
    def set_age(self,age):
        if self._age>0:
            self._age=age
        else:
            print("Invalid age")
    
    def set_marks(self,marks):
        if 0<=self.__marks<=100:
            self.__marks=marks
        else:
            print("Invalid marks(Between 0 and 100)")

    def __str__(self):
        return f"Name:{self.name},Age:{self._age},Marks:{self.__marks}"
    
s1=student("Kishan",16,90)

print(s1.name)

s1.set_age(17)
s1.set_marks(95)

print(s1)



