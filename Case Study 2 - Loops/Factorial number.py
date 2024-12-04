#Find the factorial of a given number

n = int(input('Enter a number: '))  # Input for the number to calculate factorial
fact = 1  # Initialize the factorial to 1 (since factorial of 0 and 1 is 1)
for i in range(1, n + 1):  # Loop through numbers from 1 to n
    fact = fact * i  # Multiply the current value of fact by the current number (i)
print(fact)  # Output the final factorial
