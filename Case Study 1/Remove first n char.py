#Remove first n characters from a string

# Get a string input from the user
str = input('Enter a string: ')

# Get the number of characters to remove from the beginning
n = int(input('Enter the number of first characters to be removed: '))

# Slice the string to exclude the first 'n' characters and print the result
print(str[n:])
