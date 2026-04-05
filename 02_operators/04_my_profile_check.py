# This program covers Topic Membership and Identity
# This program checks my profile details

# my skills
skills = "python django sql"

# membership
knows_python = "python" in skills
knows_java = "java" in skills

# identity
a = 100
b = 100
list1 = [1, 2]
list2 = [1, 2]

same_number = a is b
same_list = list1 is list2

# printing results
print("\n--- Skill Check ---")
print("Do I know Python:", knows_python)
print("Do I know Java:", knows_java)

print("\n--- Identity Check ---")
print("a is b:", same_number)
print("list1 is list2:", same_list)