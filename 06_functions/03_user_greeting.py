'''
Create a function to generate a welcome message.
Take user name and city as parameters
Return a formatted greeting message
Print the message
'''

def create_greeting(name, city):
    message = f"Hello {name}, welcome from {city}!"
    return message

# Input
user_name = input("Enter your name: ")
user_city = input("Enter your city: ")

# Function call
greeting = create_greeting(user_name, user_city)

# Output
print("\n" + greeting)