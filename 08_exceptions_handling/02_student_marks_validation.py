'''
Create a program to validate student marks input.
Take marks as input
Handle invalid input (non-number)
Ensure marks are between 0 and 100
Display valid marks
'''

try:
    marks = int(input("Enter marks (0-100): "))

    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100.")
    else:
        print("Valid marks:", marks)

except ValueError:
    print("Invalid input! Please enter a number.")

finally:
    print("Validation completed.")