#Write a Python program to convert time from 24-hour format to 12-hour format.

# Get the time in 24-hour format from the user
time = input('Enter the time in 24-hour format (HH:MM): ')

# Split the input into hours and minutes
time = time.split(':')
hours = int(time[0])  # Extract hours
minutes = int(time[1])  # Extract minutes

# Determine the AM/PM period and adjust the hour if needed
if hours == 0:
    # Midnight case: 00:XX is 12:XX AM
    hours = 12
    period = 'AM'
elif hours < 12:
    # Morning case: 01:XX to 11:XX is AM
    period = 'AM'
elif hours == 12:
    # Noon case: 12:XX is PM
    period = 'PM'
else:
    # Afternoon/evening case: 13:XX to 23:XX is PM
    hours -= 12
    period = 'PM'

# Print the converted time in 12-hour format
# Ensure minutes are always displayed as two digits
print(f'{hours}:{minutes:02d} {period}')
