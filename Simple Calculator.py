def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
    print("Select an operation: ") 
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Taking input from the user
    try:
        choice = int(input("Enter choice (1/2/3/4): "))  # Ensure integer input
        
        if choice in [1, 2, 3, 4]:  # Validate input
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print("The sum is", add(num1, num2))
            elif choice == 2:
                print("The difference is", subtract(num1, num2))
            elif choice == 3:
                print("The product is", multiply(num1, num2))
            elif choice == 4:
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print("The quotient is", divide(num1, num2))
        else:
            print("Invalid choice, please enter a number between 1 and 4.")
    
    except ValueError:
        print("Invalid input, please enter a number.")

if __name__ == "__main__":
    calculator()
