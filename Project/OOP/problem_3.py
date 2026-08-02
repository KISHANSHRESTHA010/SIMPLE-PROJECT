# Inheritance
class Animal:
    def __init__(self,name):
        self.name=name

class cat(Animal):
    def show_name(self):
        print(f"The name of your cat is {self.name}.")

class dog(Animal):
    def show_name(self):
        print(f"The name of your dog is {self.name}.")


dog=dog("Rex")
cat=cat("Wishker")

dog.show_name()
cat.show_name()