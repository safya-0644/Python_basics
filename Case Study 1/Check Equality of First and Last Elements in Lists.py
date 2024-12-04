#Check if the first and last numbers of a list are the same.

# Define two lists of numbers
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# Get the first and last elements of the first list
x1 = numbers_x[0]  # First element of numbers_x
x2 = numbers_x[-1]  # Last element of numbers_x

# Get the first and last elements of the second list
y1 = numbers_y[0]  # First element of numbers_y
y2 = numbers_y[-1]  # Last element of numbers_y

# Print the first list
print(numbers_x)

# Check if the first and last elements of the first list are equal
if x1 == x2:
    # Print True if the first and last elements are equal
    print('Result is True')
else:
    # Print False if the first and last elements are not equal
    print('Result is False')

# Print the second list
print(numbers_y)

# Check if the first and last elements of the second list are equal
if y1 == y2:
    # Print True if the first and last elements are equal
    print('Result is True')
else:
    # Print False if the first and last elements are not equal
    print('Result is False')
