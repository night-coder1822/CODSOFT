import random
import string

def generate_password(length, complexity):
    characters = ''
    if 'uppercase' in complexity:
        characters += string.ascii_uppercase
    if 'lowercase' in complexity:
        characters += string.ascii_lowercase
    if 'digits' in complexity:
        characters += string.digits
    if 'special' in complexity:
        characters += string.punctuation

    if not characters:
        return "Invalid complexity selection"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt user for input
length = int(input("Enter the desired password length: "))
print("Select password complexity:")
print("1. Uppercase letters")
print("2. Lowercase letters")
print("3. Digits")
print("4. Special characters")
choices = ["uppercase", "lowercase", "digits", "special"]

# Input validation for choices
selected_choices = input("Enter your choices (e.g., 1 2 4): ").split()
valid_choices = [choices[int(i) - 1] for i in selected_choices if 1 <= int(i) <= len(choices)]
if not valid_choices:
    print("Invalid complexity selection. Please choose at least one option.")
else:
    complexity = valid_choices

# Generate and display the password
password = generate_password(length, complexity)
print("Generated Password:", password)
