def count_vowels_and_consonants(input_string):
    # Define vowels
    vowels = "aeiouAEIOU"
    
    # Initialize counters
    vowel_count = 0
    consonant_count = 0
    
    # Iterate through each character in the string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Input from the user
user_input = input("Enter a string: ")

# Count vowels and consonants
vowels, consonants = count_vowels_and_consonants(user_input)

# Display the result
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")