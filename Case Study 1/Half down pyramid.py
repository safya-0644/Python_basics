#Program with Nested Loops to Print a Pattern of Stars

# Nested loops to print a pattern of stars
for i in range(6):  # Outer loop to control the rows
    for j in range(i - 1, 5):  # Inner loop to control the columns
        print('*', end=' ')  # Print '*' without moving to a new line
    print()  # Move to the next line after each row
