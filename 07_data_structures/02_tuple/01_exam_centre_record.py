'''
Create a program to store exam centre details using a tuple.
Store centre name, city, and total seats in a tuple
Display all values
Try to update the number of seats and observe what happens
Create a new tuple with updated seats and display it
'''

# Creating tuple
exam_centre = ("ABC Public School", "Delhi", 120)

# Displaying tuple
print("Exam Centre Details:", exam_centre)

# Accessing values
print("Centre Name:", exam_centre[0])
print("City:", exam_centre[1])
print("Total Seats:", exam_centre[2])

# Try to update (This will not work as tuple is immutable)
# exam_centre[2] = 150   # Uncommenting this line will give error

print("\nTuples are immutable, so values cannot be changed directly.")

# Create new tuple with updated seats
updated_exam_centre = (exam_centre[0], exam_centre[1], 150)

print("Updated Exam Centre Details:", updated_exam_centre)