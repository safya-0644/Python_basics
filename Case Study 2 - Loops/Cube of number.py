#Calculate the cube of all numbers from 1 to a given number

n = int(input('Enter the values of starting range: '))  # Input the range value
for i in range(1, n+1):  # Loop from 1 to n
    print(f'Current number is: {i} and the cube is: {i**3}')  # Print number and its cube
