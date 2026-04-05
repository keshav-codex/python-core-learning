'''
Password validator and processing with enhanced checks.
Password length ≥ 8 characters.
Must include at least one number, one special character, and one uppercase letter.
Must not contain spaces.
'''

special_chars = "!@#$%^&*"

while True:
    password = input("Enter your password: ").strip()

    # Validation checks
    has_number = any(char.isdigit() for char in password)
    has_special = any(char in special_chars for char in password)
    has_upper = any(char.isupper() for char in password)
    has_space = " " in password

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not has_number:
        print("Password must contain at least one number.")
    elif not has_special:
        print("Password must contain at least one special character (!@#$%^&*).")
    elif not has_upper:
        print("Password must contain at least one uppercase letter.")
    elif has_space:
        print("Password must not contain spaces.")
    else:
        print("Password is valid!")
        break  # Exit loop if valid

# Show password in upper and lower case
print("Password in uppercase:", password.upper())
print("Password in lowercase:", password.lower())

# Replace special characters with '*'
cleaned_password = password
for char in special_chars:
    cleaned_password = cleaned_password.replace(char, '*')
print("Cleaned password:", cleaned_password)