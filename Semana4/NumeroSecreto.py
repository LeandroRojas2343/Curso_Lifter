import random

# Function to generate a new random number from 1 to 10
def new_number():
    return random.randint(1, 10)

# Generate a secret number
secret_num = new_number()

# Ask the user to input a number
user_num = input("Enter a number (1-10): ")

# Game loop using the provided condition
while (secret_num != int(user_num)):

    try:
        user_num = int(user_num)
    except ValueError:
        print("Please enter a valid number.")
        user_num = input("Enter a number (1-10): ")
        continue

    if user_num < secret_num:
        print("It's higher.")
    elif user_num > secret_num:
        print("It's lower.")

    # Ask again
    user_num = input("Enter a number (1-10): ")

print("You guessed it!")





