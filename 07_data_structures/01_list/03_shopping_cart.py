'''
Create a list of 5 items
Add a new item using append()
Remove any item using pop(index)
Display first 3 items using slicing
Sort items alphabetically
'''

cart = []

# Take 5 items
for i in range(1, 6):
    item = input(f"Enter item {i}: ")
    cart.append(item)

print("\nShopping cart:", cart)

# Add new item
new_item = input("Enter item to add: ")
cart.append(new_item)

print("After adding item:", cart)

# Remove item using index
remove_index = int(input("Enter index to remove item (0-based): "))
cart.pop(remove_index)

print("After removing item:", cart)

# Show first 3 items using slicing
print("First 3 items:", cart[:3])

# Sort items
cart.sort()
print("Sorted cart:", cart)