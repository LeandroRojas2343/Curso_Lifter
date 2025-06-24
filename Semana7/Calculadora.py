def show_menu(): 
    print("\nCalculator")
    print("Current number:", current_number)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Clear result")
    print("6. Exit")

current_number = 0.0 

while True:
    show_menu()
    option = input("Select an option (1-6): ")

    if option == "6":
        print("Goodbye")
        break 

    if option not in ["1", "2", "3", "4", "5"]:
        print("Invalid option. Please select from 1 to 6.")
        continue

    if option == "5": 
        current_number = 0.0 
        print("Result cleared.")
        continue

    new_value = input("Enter a number: ")
    try: 
        new_value = float(new_value)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    if option == "1": 
        current_number += new_value
    elif option == "2":
        current_number -= new_value
    elif option == "3": 
        current_number *= new_value
    elif option == "4":
        if new_value == 0:
            print("Error: Cannot divide by 0.")
            continue
        current_number /= new_value

    print("New result:", current_number)

  
        




