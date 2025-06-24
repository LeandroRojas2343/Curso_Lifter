def show_menu(result):
    print("\nCalculator")
    print("Current result:", result)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset result")
    print("6. Exit")

def get_option(): 
    return input("Choose an option (1-6): ")

def get_number(): 
    try:
        return float(input("Enter a number: "))
    except ValueError: 
        print("Error: Invalid number.")
        return None 

def calculate(result, option, number): 
    if option == "1": 
        return result + number
    elif option == "2": 
        return result - number 
    elif option == "3": 
        return result * number 
    elif option == "4": 
        if number == 0: 
            print("Error: Cannot divide by zero.")
            return result 
        return result / number 
    return result 

def calculator(): 
    result = 0.0 
    while True: 
        show_menu(result)
        option = get_option()

        if option == "6": 
            print("Goodbye.")
            break 
        elif option == "5": 
            result = 0.0 
            print("Result reset.")
            continue
        elif option not in ["1", "2", "3", "4"]: 
            print("Invalid option.")
            continue

        number = get_number()
        if number is None:
            continue

        result = calculate(result, option, number)
        print("New result:", result)

# Run
calculator()
            
         


    
  
        




