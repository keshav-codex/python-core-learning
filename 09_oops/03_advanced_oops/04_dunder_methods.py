# Dunder (Magic) Methods in Python OOP

# These are special methods that start and end with __
# They allow us to define how objects behave with built-in operations


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # String representation for user (print)
    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

    # Official representation (debugging)
    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

    # Length of object
    def __len__(self):
        return len(self.name)

    # Addition of two Student objects (marks add)
    def __add__(self, other):
        return self.marks + other.marks

    # Equality check
    def __eq__(self, other):
        return self.marks == other.marks


# Creating objects
s1 = Student("Amit", 80)
s2 = Student("Ravi", 90)
s3 = Student("Amit", 80)

# __str__
print(s1)

# __repr__
print(repr(s1))

# __len__
print(len(s1))  # length of name

# __add__
print(s1 + s2)  # marks addition

# __eq__
print(s1 == s2)
print(s1 == s3)