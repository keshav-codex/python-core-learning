'''
Create a function to calculate total shopping bill.
Take price of 3 items as parameters
Add GST (assume 18%)
Return final amount
Call function and print bill
'''

def calculate_bill(price1, price2, price3):
    total = price1 + price2 + price3
    gst = total * 0.18
    final_amount = total + gst
    return final_amount


# Input
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

# Function call
bill = calculate_bill(item1, item2, item3)

# Output
print("\nFinal Bill (including GST):", bill)