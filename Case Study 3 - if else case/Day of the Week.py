#Write a Python program that maps a number (1-7) to a day of the week.

# Define a dictionary mapping numbers to days of the week
days = {
    1: 'Sunday',
    2: 'Monday',
    3: 'Tuesday',
    4: 'Wednesday',
    5: 'Thursday',
    6: 'Friday',
    7: 'Saturday'
}

# Get the number input from the user
n = int(input('Enter a number (1-7): '))

# Check if the number is valid (between 1 and 7)
if 1 <= n <= 7:
    # Print the corresponding day of the week
    print(f'The day of the week for the number {n} is {days[n]}')
else:
    # Handle invalid input
    print('Invalid number. Please enter a number between 1 and 7.')
