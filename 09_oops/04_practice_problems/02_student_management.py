# Student Management System using OOP

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def show_details(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")


class StudentSystem:
    def __init__(self):
        self.students = []

    # Add student
    def add_student(self, roll_no, name, marks):
        student = Student(roll_no, name, marks)
        self.students.append(student)
        print("Student added successfully")

    # Show all students
    def show_all(self):
        if not self.students:
            print("No students found")
            return

        for student in self.students:
            student.show_details()

    # Search student by roll number
    def search_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                student.show_details()
                return
        print("Student not found")

    # Delete student
    def delete_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student deleted successfully")
                return
        print("Student not found")


# ---------------- Test Code ----------------

system = StudentSystem()

system.add_student(1, "Amit", 85)
system.add_student(2, "Ravi", 90)
system.add_student(3, "Neha", 88)

print("\nAll Students:")
system.show_all()

print("\nSearch Student:")
system.search_student(2)

print("\nDelete Student:")
system.delete_student(1)

print("\nAfter Deletion:")
system.show_all()