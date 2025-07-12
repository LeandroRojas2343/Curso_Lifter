# Enter the number of grades
n = int(input("Enter the number of grades: "))

# List to store the grades
grades = []

# Entering grades
for i in range(n):
    grade = float(input(f"Enter grade #{i+1}: "))
    grades.append(grade)

# Classification of grades
passed = [grade for grade in grades if grade >= 70]
failed = [grade for grade in grades if grade < 70]

# Calculations
total_passed = len(passed)
total_failed = len(failed)
average_total = sum(grades) / len(grades) if grades else 0
average_passed = sum(passed) / len(passed) if passed else 0
average_failed = sum(failed) / len(failed) if failed else 0

# Results
print(f"\nNumber of passed grades: {total_passed}")
print(f"Number of failed grades: {total_failed}")
print(f"Average of all grades: {average_total:.2f}")
print(f"Average of passed grades: {average_passed:.2f}")
print(f"Average of failed grades: {average_failed:.2f}")