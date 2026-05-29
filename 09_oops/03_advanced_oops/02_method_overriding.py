# Method Overriding in Python

# Parent class
class Animal:
    def sound(self):
        print("Animal makes a sound")


# Child class
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Another child class
class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Creating objects
a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()