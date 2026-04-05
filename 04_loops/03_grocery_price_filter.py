# This program calculates total price for valid grocery items demonstrated break and continue

total_price = 0

for i in range(1, 6):
    price = float(input(f"Enter price of item {i}: "))
    
    if price == 0:
        print("Input stopped")
        break
    if price > 1000:
        print("Item too expensive, skipped")
        continue
    
    total_price += price

print("\nTotal price of valid items:", total_price)