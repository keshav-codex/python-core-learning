#Topic: Inheritance in Python

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):
    def speak(self):
        print(self.name, "barks")


class Cat(Animal):
    def speak(self):
        print(self.name, "meows")


# Creating objects
d1 = Dog("Tommy")
c1 = Cat("Kitty")

d1.speak()
c1.speak()