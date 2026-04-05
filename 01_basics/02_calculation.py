# This program performs basic operations using different data types

# taking input
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# converting to integer
num1 = int(num1)
num2 = int(num2)

# performing operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# using float (average)
average = (num1 + num2) / 2

# using boolean
is_equal = num1 == num2

# using string
message = "Calculation completed"

# printing results
print("\n--- Results ---")
print("First number:", num1)
print("Second number:", num2)

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Average:", average)

print("Are both numbers equal:", is_equal)
print("Message:", message)

# printing data types
print("\n--- Data Types ---")
print("Type of num1:", type(num1))
print("Type of division:", type(division))
print("Type of average:", type(average))
print("Type of is_equal:", type(is_equal))