  # Pseudocodigo1

# Ask the user for the price
price = float(input("Enter price: "))

# Calculate the discount based on the price value
if price >= 100:
    discount = price * 0.10  # 10%
else:
    discount = price * 0.02  # 2%

# Calculate the final price with the discount applied
final_price = price - discount

# Display the final result
print("Original price:", price)
print("Discount applied:", discount)
print("Final price with discount:", final_price)


