'''
Take 5 expenses as input and store in a list
Add one more expense using append()
Remove the last expense using pop()
Sort all expenses
Display the final list
'''

expenses = []

# Take 5 expenses
for i in range(1, 6):
    amount = float(input(f"Enter expense {i}: "))
    expenses.append(amount)

print("\nExpenses list:", expenses)

# Add one more expense
new_expense = float(input("Enter one more expense: "))
expenses.append(new_expense)

print("After adding new expense:", expenses)

# Remove last expense
expenses.pop()
print("After removing last expense:", expenses)

# Sort expenses
expenses.sort()
print("Sorted expenses:", expenses)