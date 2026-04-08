'''
Create a function to calculate total and average marks.
Take marks of 3 subjects as parameters
Return total and average
Call the function and display results
'''

def calculate_marks(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    return total, average


# Input
mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

# Function call
total_marks, avg_marks = calculate_marks(mark1, mark2, mark3)

# Output
print("\nTotal Marks:", total_marks)
print("Average Marks:", avg_marks)