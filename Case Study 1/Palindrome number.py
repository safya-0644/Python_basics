#Program to Check if a Number is a Palindrome

# Get an integer input from the user
num = int(input('Enter a value: '))

# Convert the integer to a string for easier comparison
st_num = str(num)

# Check if the string is equal to its reverse
if st_num == st_num[::-1]:
    # Print if the number is a palindrome
    print('The given number is a palindrome')
else:
    # Print if the number is not a palindrome
    print('The given number is not a palindrome')
