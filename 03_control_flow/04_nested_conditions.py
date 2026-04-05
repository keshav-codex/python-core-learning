# This program checks job eligibility by using nested condition.

age = int(input("Enter your age: "))
degree = input("Do you have a degree (yes/no): ")
experience = int(input("Enter years of experience: "))

if age >= 21:
    if degree == "yes":
        if experience > 5:
            print("You are eligible for the job and have strong experience")
        elif experience >= 2:
            print("You are eligible for the job")
        else:
            print("You need more experience")
    else:
        print("Degree is required")
else:
    print("You are too young")