# Program to print the multiplication table from 1 to 10

# Print the header row with numbers from 1 to 10
print("    ", end='')  # Adding space for alignment
for i in range(1, 11):
    print(f"{i:4}", end='')  # Print column headers (1-10)
print()  # New line after headers

# Print a separator line
print("    " + "----" * 10)

# Outer loop for the rows (1 to 10)
for i in range(1, 11):
    # Print the row header
    print(f"{i:2} |", end='')  # Print row label (1-10) with a separator '|'
    
    # Inner loop for the columns (1 to 10)
    for j in range(1, 11):
        # Multiply the row number by the column number
        result = i * j
        # Print the result with proper formatting, width of 4 characters
        print(f"{result:4}", end='')  # Print each result aligned with spaces
    # Move to the next line after completing the row
    print()
