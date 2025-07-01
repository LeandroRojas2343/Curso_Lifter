

#Sums between data 
print("Sum of an int + a float")
sum1 = 4
sum2 = 23.56
print("x + y =", x + y)  # 27.56

print("String + string sum")
greeting = "Hello"
name = "World"
print(greeting + " " + name)  # "Hello World"

print("Sum of an int + string")
text = "Age: "
number = 30
print(text + str(number))  # Result: "Age: 30"

print("Convert string to int")
text = "The number is: "
number = 5
result = text + str(number)
print(result)

print("Sum list + list")
list1 = [1, 4, 5]
list2 = [2, 6, 4]
result = list1 + list2
print(f"""
--- Result of List Concatenation ---
List 1: {list1} (length: {len(list1)})
List 2: {list2} (length: {len(list2)})

Concatenated List: {result} (total length: {len(result)})
""")  # Just experimenting with this print

print("String + list")
text = "List elements: "
list_values = [2, 3, 6]
# list to string
result = text + str(list_values)
print(result)

print("float + int")
float_num = 2.34
int_num = 4
result = int_num + float_num
print(f"Result of adding {float_num} + {int_num} = {result} (type: {type(result)})")

# Sum of two booleans
sum1 = True
sum2 = False
sum_bool = a + b
print("Result:", sum_bool)