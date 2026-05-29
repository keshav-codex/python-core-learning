# Topic: Methods in OOP

class Student:
    school_name = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

    # Class method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    # Static method
    @staticmethod
    def welcome_message():
        print("Welcome to the Student Management System")


# Creating object
s1 = Student("Amit", 20)

# Instance method call
s1.show_details()

print("\nSchool Name (before):", Student.school_name)

# Class method call
Student.change_school("XYZ School")

print("School Name (after):", Student.school_name)

print()

# Static method call
Student.welcome_message()