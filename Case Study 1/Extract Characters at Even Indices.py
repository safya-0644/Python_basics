#Print characters present at an even index number

# Get a string input from the user
str = input('Enter a string value: ')

# Get the length of the string
s = len(str)

# Loop through the string using the length
for i in range(s):
    # Check if the current index is even
    if i % 2 == 0:
        # Print the character at the even index
        print(str[i])
