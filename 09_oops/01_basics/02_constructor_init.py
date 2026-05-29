# Topic: Constructor (__init__) in OOP

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


s1 = Student("Amit", 20)
s2 = Student("Rahul", 22)

print("----- Student Records -----")
print(f"Name: {s1.name}, Age: {s1.age}")
print(f"Name: {s2.name}, Age: {s2.age}")