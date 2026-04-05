"""
This program prints weekly study hours for 5 subjects witsimilar to real-world validation:
- Each subject hours: 0 to 24
- Total hours per day <= 24
"""

for day in range(1, 8):
    print(f"\nDay {day}:")
    total_day_hours = 0

    for subject in range(1, 6):
        while True:
            hours = int(input(f"  Enter hours studied for subject {subject}: "))

            # check if hours are valid
            if hours < 0 or hours > 24:
                print("    Invalid hours! Must be between 0 and 24. Try again.")
            elif total_day_hours + hours > 24:
                print("Total hours for the day cannot exceed 24 hours")
            else:
                total_day_hours += hours
                break  # exit the while loop when valid

    print(f"Total study hours for Day {day}: {total_day_hours}")