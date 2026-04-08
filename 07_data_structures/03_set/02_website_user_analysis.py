'''
Create a program to analyze users visiting two different days on a website.
Take 5 user IDs for Day 1
Take 5 user IDs for Day 2
Find:
    Total unique users (union)
    Returning users (intersection)
    New users on Day 2
    Users who visited only Day 1
    Check if Day 2 users are subset of Day 1
'''

# Program: Website user analysis using set

day1_users = set()
day2_users = set()

# Input for Day 1
print("Enter user IDs for Day 1:")
for i in range(1, 6):
    user = input(f"User {i}: ")
    day1_users.add(user)

# Input for Day 2
print("\nEnter user IDs for Day 2:")
for i in range(1, 6):
    user = input(f"User {i}: ")
    day2_users.add(user)

print("\nDay 1 Users:", day1_users)
print("Day 2 Users:", day2_users)

# Union
all_users = day1_users.union(day2_users)
print("\nTotal Unique Users:", all_users)

# Intersection
returning_users = day1_users.intersection(day2_users)
print("Returning Users:", returning_users)

# Difference
new_users = day2_users.difference(day1_users)
print("New Users on Day 2:", new_users)

only_day1 = day1_users.difference(day2_users)
print("Users only on Day 1:", only_day1)

# Subset check
is_subset = day2_users.issubset(day1_users)
print("Are Day 2 users subset of Day 1:", is_subset)