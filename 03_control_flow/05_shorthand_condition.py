# This program checks interview eligibility using short-hand

experience = int(input("Enter your experience (years): "))
salary = int(input("Enter your expected salary: "))

# short-hand condition
print("Eligible for interview") if experience >= 2 else print("Not eligible")

# another short-hand
print("High salary expectation") if salary > 50000 else print("Salary is acceptable")