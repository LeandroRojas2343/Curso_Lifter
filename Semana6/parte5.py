def count_upper_lower(text):
    upper = 0
    lower = 0

    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    print(f"There are {upper} upper case letters and {lower} lower case letters.")

# Here the user can enter the text
user_input = input("Enter a text: ")
count_upper_lower(user_input)


