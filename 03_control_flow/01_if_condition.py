# This program checks login with if conditions

correct_password = "1234"
password = input("Enter your password: ")

if password == "":
    print("Password not entered")

if password != "":
    print("Password entered")

if password != correct_password:
    print("Wrong Password : Login unsuccessful")

if password == correct_password:
    print("Login successful")