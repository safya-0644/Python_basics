#Print multiplication table of a given number

# Taking the base number for multiplication
n = int(input('Enter a number: '))

# Taking the range limit for the multiplication table
t = int(input('Enter the range value: '))

# Loop to print the multiplication table up to the specified range
for i in range(1, t + 1):
    mul = n * i  # Multiplying the number n by i
    print(f'{n} * {i} = {mul}')  # Printing the multiplication in a readable format
