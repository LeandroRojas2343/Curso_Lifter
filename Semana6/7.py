def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

# Example
input_list = [1, 4, 6, 7, 13, 9, 67]
result = filter_primes(input_list)
print("Prime numbers:", result)  # Output: Prime numbers: [7, 13, 67]


