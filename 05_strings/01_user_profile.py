# Program: Demonstrate simple string operations on user profile.

# Input name, age, email
full_name = input("Enter your full name: ").strip()
age_input = input("Enter your age: ").strip()
email = input("Enter your email: ").strip()

# Name Validation (basic)
if full_name.replace(" ", "").isalpha():
    print("Valid name")
else:
    print("Name contains invalid characters!")

# Age Validation (basic)
if age_input.isdigit():
    age = int(age_input)
    if 1 <= age <= 120:
        print("Valid age")
    else:
        print("Age out of range!")
else:
    print("Invalid age input!")

# Email Validation (basic)
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email format!")

# Demonstrate string functions
print("\nProfile Summary:")
first_name = full_name.split()[0]      # first name
last_name = full_name.split()[-1]      # last name
print("First Name:", first_name)
print("Last Name:", last_name)
print("Age:", age_input)
print("Email:", email.lower())

print("\nString operations examples:")
print("Full name in uppercase:", full_name.upper())
print("Full name in lowercase:", full_name.lower())
print("Number of characters (excluding spaces):", len(full_name.replace(" ", "")))
print("First letter of first name:", first_name[0])
print("Last 2 letters of last name:", last_name[-2:])