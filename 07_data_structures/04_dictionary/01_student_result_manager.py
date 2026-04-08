'''
Create a program to manage student marks using a dictionary.
Store 5 subjects with marks
Display all subjects and marks
Update marks of a subject
Delete a subject
Calculate total and average marks
'''

student_marks = {}

# Input 5 subjects
for i in range(1, 6):
    subject = input(f"Enter subject {i}: ")
    marks = int(input(f"Enter marks for {subject}: "))
    student_marks[subject] = marks

print("\nStudent Marks:", student_marks)

# Display all subjects
print("\nSubjects and Marks:")
for subject, marks in student_marks.items():
    print(subject, ":", marks)

# Updating marks
update_subject = input("\nEnter subject to update marks: ")
if update_subject in student_marks:
    new_marks = int(input("Enter new marks: "))
    student_marks[update_subject] = new_marks

print("Updated Marks:", student_marks)

# Deleting subject
delete_subject = input("\nEnter subject to delete: ")
if delete_subject in student_marks:
    del student_marks[delete_subject]

print("After Deletion:", student_marks)

# Total and average
total = sum(student_marks.values())
average = total / len(student_marks)

print("\nTotal Marks:", total)
print("Average Marks:", average)