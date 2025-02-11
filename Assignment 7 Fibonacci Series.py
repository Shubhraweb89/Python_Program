def fibonacci(n):
    # Initialize the first two terms of the Fibonacci series
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci series up to n terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence[:n]

# Input from the user
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))

# Check if the input is valid
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    # Generate and display the Fibonacci series
    fib_series = fibonacci(num_terms)
    print(f"Fibonacci series up to {num_terms} terms: {fib_series}")