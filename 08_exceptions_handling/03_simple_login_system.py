'''
Create a simple login system.
Take username and password
Convert password input to integer (simulate PIN)
Handle invalid input
Check credentials and display result
'''

try:
    username = input("Enter username: ")
    password = int(input("Enter PIN (numbers only): "))

    if username == "admin" and password == 1234:
        print("Login successful!")
    else:
        print("Invalid credentials.")

except ValueError:
    print("PIN must be a number!")

finally:
    print("Login process completed.")