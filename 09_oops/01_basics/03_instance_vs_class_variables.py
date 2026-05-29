# Topic: Instance Variables vs Class Variables in OOP

class Student:
    # Class variable (shared)
    school_name = "ABC School"

    def __init__(self, name, age):
        # Instance variables (unique for each object)
        self.name = name
        self.age = age


# Creating objects
s1 = Student("Amit", 20)
s2 = Student("Rahul", 22)

# Instance variables
print("Instance Variables:")
print(s1.name, s1.age)
print(s2.name, s2.age)

# Class variable (shared)
print("\nClass Variable:")
print(s1.school_name)
print(s2.school_name)