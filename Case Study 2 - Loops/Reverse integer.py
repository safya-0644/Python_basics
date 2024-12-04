#Reverse a integer number

n = int(input('Enter the integer: '))  # Input the integer to reverse
rev = 0  # Initialize a variable to store the reversed number
while n != 0:  # Loop until the number becomes 0
    rem = n % 10  # Get the last digit of the number
    rev = rev * 10 + rem  # Build the reversed number by shifting current digits and adding the last digit
    n = n // 10  # Remove the last digit from the number
print(rev)  # Output the reversed number
