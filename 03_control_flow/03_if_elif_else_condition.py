# This program checks performance by using if elif else condition.

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
    print("Excellent performance")
elif marks >= 75:
    print("Grade: B")
    print("Good performance")
elif marks >= 50:
    print("Grade: C")
    print("Average performance")
elif marks >= 40:
    print("You passed the exam")
else:
    print("Grade: Fail")
    print("Need improvement")