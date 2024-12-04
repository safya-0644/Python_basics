#Write a Python program to print the reverse number pattern using a for loop.

for i in range(6, 0, -1):  # Outer loop (controls the number of rows)
    for j in range(i, 0, -1):  # Inner loop (prints numbers in descending order)
        print(j, end='')  # Print each number without a new line
    print()  # Move to the next line after each row
