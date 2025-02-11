import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")

while True:
    try:
        guess = int(input("Enter your guess: "))  # Take user input

        if guess < secret_number:
            print("Too Low! Try again.")
        elif guess > secret_number:
            print("Too High! Try again.")
        else:
            print(f"Congratulations! You guessed it right. The number was {secret_number}.")
            break  # Exit loop when the user guesses correctly
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 100.")