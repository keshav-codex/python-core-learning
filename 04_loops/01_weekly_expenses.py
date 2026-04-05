# This program calculates weekly expenses by using for loop and range()

total_expense = 0

for day in range(1, 8):
    expense = float(input(f"Enter expense for day {day}: "))
    total_expense += expense

print("\nTotal weekly expense:", total_expense)