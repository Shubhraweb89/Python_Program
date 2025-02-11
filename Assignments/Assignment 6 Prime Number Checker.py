def is_prime(n):
    # Check if the number is less than 2 (not prime)
    if n < 2:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Input from the user
num = int(input("Enter a number to check if it is prime: "))

# Check and display the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")