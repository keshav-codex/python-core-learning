'''
Display formatted greeting message with validation
Name cannot be empty and must contain only letters.
Age must be between 1 and 120.
Course cannot be empty.
'''

# Validate Name
while True:
    name = input("Enter your name: ").strip()
    if name.isalpha():
        break
    else:
        print("Invalid name! Only letters allowed.")

# Validate Age
age_str = ""
while True:
    age_str = input("Enter your age: ").strip()
    if age_str.isdigit():
        age = int(age_str)
        if 1 <= age <= 120:
            break
        else:
            print("Invalid age! Must be between 1 and 120.")
    else:
        print("Invalid input! Enter digits only.")

# Validate Course
while True:
    course = input("Enter your course: ").strip()
    if course != "":
        break
    else:
        print("Course cannot be empty.")

# Using f-string
print(f"\nHello {name}!\nAge: {age}\nCourse: {course}")

# Using format method
print("\nUsing format method:")
print("Hello {}\nAge: {}\nCourse: {}".format(name, age, course))

# Using escape characters
print("\nSpecial message with escape characters:")
print("Welcome to the course!\n\tEnjoy learning \"{}\"!".format(course))