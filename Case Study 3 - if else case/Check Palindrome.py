#Write a Python program that checks whether a given string is a palindrome.

# Get input from the user
st_value = input('Enter a value: ').strip()

# Convert input to lowercase for consistent comparison
st_low = st_value.lower()

# Check if the input is a palindrome
if st_low == st_low[::-1]:
    print('The given value is a palindrome.')
else:
    print('The given value is not a palindrome.')
