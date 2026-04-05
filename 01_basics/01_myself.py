# This program shows my basic information

# storing my details
first_name = "Keshav"
last_name = "Jha"
age = "26"
city = 'Delhi'
is_student = True
course = "Python"
daily_hours = 3

# printing my details in simple way

print("Printing in simple way")
print("My First name is:", first_name)
print("My last name is:", last_name)
print("My age is:", age)
print("I live in:", city)
print("Am I a student:", is_student)
print("I am learning", course)
print("I study for",daily_hours," hours daily")

# printing types

print("\nPrinting Data Types")
print("Type of first name:", type(first_name))
print("Type of last name:", type(last_name))
print("Type of age:", type(age))
print("Type of city:", type(city))
print("Type of is_student:", type(is_student))
print("Type of course:", type(course))
print("Type of daily_hours:", type(daily_hours))

# print using f-string style

print("\nPrinting using f-string")
print(f"My First name is: {first_name}")
print(f"My last name is: {last_name}")
print(f"My age is: {age}")
print(f"I live in: {city}")
print(f"Am I a student: {is_student}")
print(f"I am learning {course}")
print(f"I study for {daily_hours} hours daily\n")

# print using single print() with print function

print("Printing using f-string and single print()")
print(f"""
My First name is: {first_name}
My last name is: {last_name}
My age is: {age}
I live in: {city}
Am I a student: {is_student}
I am learning {course}
I study for {daily_hours} hours daily\n
""")

# print using format() style

print("Printing using formate()\n")
print("My First name is: {}".format(first_name))
print("My last name is: {}".format(last_name))
print("My age is: {}".format(age))
print("I live in: {}".format(city))
print("Am I a student: {}".format(is_student))
print("I am learning {}".format(course))
print("I study for {} hours daily".format(daily_hours))

# print using sinle print() and formate()

print("\nPrinting using formate() and single print()")
print("""
My First name is: {}
My last name is: {}
My age is: {}
I live in: {}
Am I a student: {}
I am learning {}
I study for {} hours daily
""".format(first_name, last_name, age, city, is_student, course, daily_hours))