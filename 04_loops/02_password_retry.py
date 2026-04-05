# This program keeps asking for password until correct by using while and break

correct_password = "1234"

while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful")
        break
    else :
        print("Wrong Password")