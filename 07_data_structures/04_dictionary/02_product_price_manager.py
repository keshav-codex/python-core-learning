'''
Create a program to manage product prices in a shop.
Store product names and prices
Add a new product
Update price of a product
Remove a product
Display all products
Find the most expensive product
'''

products = {}

# Input 4 products
for i in range(1, 5):
    name = input(f"Enter product {i} name: ")
    price = float(input(f"Enter price of {name}: "))
    products[name] = price

print("\nProduct List:", products)

# Add new product
new_name = input("\nEnter new product name: ")
new_price = float(input("Enter price: "))
products[new_name] = new_price

print("After Adding:", products)

# Update price
update_name = input("\nEnter product name to update price: ")
if update_name in products:
    new_price = float(input("Enter new price: "))
    products[update_name] = new_price

print("After Update:", products)

# Remove product
remove_name = input("\nEnter product name to remove: ")
if remove_name in products:
    del products[remove_name]

print("After Removal:", products)

# Display all products
print("\nAll Products:")
for name, price in products.items():
    print(name, ":", price)

# Find most expensive product
max_product = max(products, key=products.get)
print("\nMost Expensive Product:", max_product)
print("Price:", products[max_product])