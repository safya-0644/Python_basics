#Write a Python program that checks whether a given character is a vowel or consonant.

# Get a single character from the user
c = input('Enter a character: ')

# Check for valid input
if len(c) != 1:
    print('Invalid input! Please enter a single character.')
elif c.isdigit():
    print('Invalid input! Please enter a letter, not a digit.')
elif c.lower() in ['a', 'e', 'i', 'o', 'u']:
    # Check if the character is a vowel
    print('The given character is a vowel.')
elif c.isalpha():
    # Check if the character is a consonant
    print('The given character is a consonant.')
else:
    # Handle any other unexpected input
    print('Invalid input! Please enter an alphabetic character.')
