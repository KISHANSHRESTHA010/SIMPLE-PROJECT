# sub class overriding

class Animal:
    def __init__(self,name):
        self.name=name

    def speak(self):
        print(f'{Animal} makes a sound')

class dog(Animal):
    def speak(self):
        print(f"{self.name} makes woooof!")

dog=dog("Rex")

dog.speak()