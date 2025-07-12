
#Pseudocodigo2 
# Start

# Ask for seconds
seconds = int(input("Enter the number of seconds: "))

# Conditions
if seconds == 600:
    print("Equal")
    result = 0  # The result is 0
elif seconds > 600:
    print("Greater")
    result = seconds - 600
    print(f"You exceeded the 10 minutes by {result} seconds.")
else:
    print("Less")
    result = 600 - seconds
    print(f"{result} seconds are missing to reach 10 minutes.")

# End