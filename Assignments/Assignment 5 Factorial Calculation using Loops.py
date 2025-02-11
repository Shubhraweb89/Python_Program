# Taking user input for a number
n = int(input("Enter any number: "))  

# Initializing factorial variable to 1 (since factorial of 0 is 1)
fact = 1  

# Loop from 1 to n (inclusive) to calculate factorial
for i in range(1, n + 1):  
    fact = fact * i  # Multiply current value of fact with i

# Print the calculated factorial
print("Factorial is", fact)
