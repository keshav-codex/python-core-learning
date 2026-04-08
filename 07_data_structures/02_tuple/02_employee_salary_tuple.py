'''
Create a program to manage employee salary details using tuple packing and unpacking.
Take basic salary, bonus, and allowance as input
Pack them into a tuple
Unpack values into separate variables
Calculate total salary and display all values
'''

# Taking input
basic = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))
allowance = float(input("Enter allowance: "))

# Packing into tuple
salary = (basic, bonus, allowance)

print("\nPacked Tuple:", salary)

# Unpacking
basic_salary, bonus_amount, allowance_amount = salary

# Calculate total salary
total_salary = basic_salary + bonus_amount + allowance_amount

# Display values
print("\nSalary Breakdown:")
print("Basic Salary:", basic_salary)
print("Bonus:", bonus_amount)
print("Allowance:", allowance_amount)
print("Total Salary:", total_salary)