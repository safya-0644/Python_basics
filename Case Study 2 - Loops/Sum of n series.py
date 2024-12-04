#Calculate sum of all numbers from 1 to a given number

# Taking input from the user for the number n
n = int(input('Enter a number: '))

# Initializing the sum variable
sum = 0

# Loop to calculate the sum of integers from 1 to n
for i in range(1, n + 1):
    sum = sum + i  # Adding i to sum in each iteration

# Printing the result
print(sum)
