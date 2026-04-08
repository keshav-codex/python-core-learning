
'''Create a function to calculate simple interest.
Take principal, rate, and time as parameters
Return the calculated interest
Print the result
'''

def calculate_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Input
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

# Function call
si = calculate_interest(p, r, t)

# Output
print("\nSimple Interest:", si)