# Create a program that asks the user for three numbers and displays the largest one
nuemro1 = float(input("Enter the first number: "))
numero2 = float(input("Enter the second number: "))
numero3 = float(input("Enter the third number: "))

# Condition to select the largest number

mayor = nuemro1
if numero2 > mayor:
    mayor = numero2
    if numero3 > mayor:
        mayor = numero3

print("The largest number is:", mayor)

  