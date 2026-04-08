'''
Create a program to analyze courses selected by two students.
Take 4 courses for Student A
Take 4 courses for Student B
Find:
    All courses (union)
    Common courses (intersection)
    Courses only in A (difference)
    Courses only in B (difference)
    Check if both selected same courses
'''

# Program: Student course analysis using set

student_a = set()
student_b = set()           

# Input for Student A
print("Enter courses for Student A:")
for i in range(1, 5):
    course = input(f"Course {i}: ")
    student_a.add(course)

# Input for Student B
print("\nEnter courses for Student B:")
for i in range(1, 5):
    course = input(f"Course {i}: ")
    student_b.add(course)

print("\nStudent A Courses:", student_a)
print("Student B Courses:", student_b)

# Union
all_courses = student_a.union(student_b)
print("\nAll Courses (Union):", all_courses)

# Intersection
common_courses = student_a.intersection(student_b)
print("Common Courses (Intersection):", common_courses)

# Difference
only_a = student_a.difference(student_b)
print("Courses only in A:", only_a)

only_b = student_b.difference(student_a)
print("Courses only in B:", only_b)

# Comparison
same_courses = student_a == student_b
print("Do both students have same courses:", same_courses)