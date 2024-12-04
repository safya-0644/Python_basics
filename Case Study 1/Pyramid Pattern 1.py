# Define the number of rows for the pyramid
row = 5

# Outer loop to handle the number of rows
for i in range(1, row + 1):
    # Inner loop to handle the number of columns (same as the row number)
    for j in range(1, i + 1):
        # Print the current row number, keeping it on the same line
        print(i, end=' ')
    # Move to the next line after completing one row
    print()
