#Request data

# Ask the user for data
print("Enter your first name:")
first_name = input()

print("Enter your last name:")
last_name = input()

print("Enter your age:")
age = input()

# Convert age to integer
age = int(age)

# Classify according to age
if age < 2:
    stage = "baby"
elif age < 6:
    stage = "child"
elif age < 12:
    stage = "pre-teen"
elif age < 18:
    stage = "teenager"
elif age < 30:
    stage = "young adult"
elif age < 60:
    stage = "adult"
else:
    stage = "senior adult"

# Display the result
print(f"\nHello {first_name} {last_name}, you are {age} years old and you are a {stage}.")