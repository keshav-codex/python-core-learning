# This program checks driving eligibility by using if else condition.

age = int(input("Enter your age: "))
has_license = input("Do you have a driving license (yes/no): ")

if age >= 18 and has_license == "yes":
    print("You can drive")
else:
    print("You cannot drive")

# In other way check
if age < 18:
    print("Reason: Age is less than 18")
else:
    print("Age is valid")