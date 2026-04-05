# This program checks my performance by  using Comparison and Logical operators.

# taking input
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

# comparison
passed = marks >= 40
excellent = marks > 80
low_marks = marks < 40

# logical
eligible_for_exam = (marks >= 40) and (attendance >= 75)
needs_improvement = (marks < 40) or (attendance < 75)
not_passed = not (marks >= 40)

# printing results
print("\n--- Performance Report ---")
print("Passed:", passed)
print("Excellent Performance:", excellent)
print("Low Marks:", low_marks)

print("\n--- Eligibility ---")
print("Eligible for next Exam:", eligible_for_exam)
print("Needs Improvement:", needs_improvement)
print("Not Passed:", not_passed)