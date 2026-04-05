# This program records attendance for 5 students with validation: attendance must be 0 to 100


for i in range(1, 6):
    while True:
        attendance = float(input(f"Enter attendance % for student {i}: "))

        # validate attendance
        if attendance < 0 or attendance > 100:
            print("Invalid input! Attendance must be between 0 and 100. Try again.")
        else:
            break  # exit loop if valid

    if attendance < 50:
        pass  # skip processing for low attendance.
    else:
        print(f"Attendance recorded for student {i}")