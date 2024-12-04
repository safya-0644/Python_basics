#Write a Python program to count the total number of digits in a number using a while loop.

# Taking input from the user
n = int(input('Enter a number: '))

# Initializing the counter for the number of digits
count = 0

# While loop to count the digits
while n != 0:
    n = n // 10  # Integer division removes the last digit of n
    count = count + 1  # Increment the count

# Printing the result
print(count)
