# This program calculates my monthly salary details by using Arithmetic and Assignment operator.

# taking input
salary = int(input("Enter your monthly salary: "))
bonus = int(input("Enter your bonus: "))
expenses = int(input("Enter your monthly expenses: "))

# arithmetic operations
total_income = salary + bonus
savings = total_income - expenses
double_salary = salary * 2
half_salary = salary / 2
remaining = salary % 100

# assignment operators
# salary increment
salary += 1000   

# reduced expense
expenses -= 500  

# printing results
print("\n--- My Salary Details ---")
print("Total Income:", total_income)
print("Savings:", savings)
print("Double Salary:", double_salary)
print("Half Salary:", half_salary)
print("Remaining after 100 division:", remaining)
print("\n--- Updated Values ---")
print("Updated Salary:", salary)
print("Updated Expenses:", expenses)