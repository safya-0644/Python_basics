#Print the Sum of a Current Number and a Previous number.

# Get the starting range from the user
n1 = int(input('Enter the value of the starting range: '))

# Get the ending range from the user
n2 = int(input('Enter the value of the ending range: '))

# Loop through the numbers in the given range (from n1 to n2 - 1)
for i in range(n1, n2):
    # Print the current number, the previous number, and their sum
    print(f'Current number {i} previous number {i-1} sum: {i + (i - 1)}')
