# This program simulates device settings using bitwise operators

# taking input
setting1 = int(input("Enter setting value 1: "))
setting2 = int(input("Enter setting value 2: "))

# bitwise operations
and_result = setting1 & setting2
or_result = setting1 | setting2
xor_result = setting1 ^ setting2
left_shift = setting1 << 1
right_shift = setting1 >> 1

# printing results
print("\n--- Device Settings Result ---")
print("AND Result:", and_result)
print("OR Result:", or_result)
print("XOR Result:", xor_result)
print("Left Shift:", left_shift)
print("Right Shift:", right_shift)