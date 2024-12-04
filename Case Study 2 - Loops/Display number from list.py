'''Write a Python program to display only those numbers from a list that satisfy the following conditions
The number must be divisible by five
If the number is greater than 150, then skip it and move to the following number
If the number is greater than 500, then stop the loop'''

numbers = [12, 75, 150, 180, 145, 525, 50]  # List of numbers
for num in numbers:
    if num % 5 == 0:  # Check if the number is divisible by 5
        if num > 150:  # Skip numbers greater than 150
            continue
        elif num > 500:  # Stop the loop if a number greater than 500 is encountered
            break
        print(num)  # Print the number if it passes the checks
