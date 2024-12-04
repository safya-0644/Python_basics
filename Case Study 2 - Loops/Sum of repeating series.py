#Find the sum of the series up to n terms(eg: 2+22+222+2222....)

n = int(input('Enter the terms: '))  # Input the number of terms in the series
a = int(input('Enter the series number: '))  # Input the base number to repeat in the series
sum = 0  # Initialize the sum variable to 0

for i in range(1, n+1):  # Loop through the series from 1 to n
    sum = sum + int(str(a) * i)  # Repeat the number 'a', i times, and add to sum

print(f"The sum is: {sum}")  # Print the final sum
