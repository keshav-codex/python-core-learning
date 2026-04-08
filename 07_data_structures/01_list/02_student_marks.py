'''
Take marks of 5 subjects and store in a list
Update marks of 1 subject (user choice)
Display highest and lowest marks using sorting
Show only top 3 marks using slicing
'''

marks = []

# Take marks for 5 subjects
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

print("\nMarks list:", marks)

# Updating marks
index = int(input("Enter subject number to update (1-5): ")) - 1
new_mark = int(input("Enter new marks: "))
marks[index] = new_mark

print("Updated marks list:", marks)

# Sort marks (descending)
marks.sort(reverse=True)
print("Sorted marks (highest to lowest):", marks)

#Printing top 3 marks using slicing
print("Top 3 marks:", marks[:3])