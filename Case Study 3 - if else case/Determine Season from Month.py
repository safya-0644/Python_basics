#Write a Python program to determine the season based on the given month.

# Get the month input from the user
month = input('Enter month: ')

# Determine the season based on the month
if month.lower() in ['december', 'january', 'february']:
    # Winter months
    print("It's winter season")
elif month.lower() in ['march', 'april', 'may']:
    # Summer months
    print("It's summer season")
elif month.lower() in ['june', 'july', 'august']:
    # Monsoon months
    print("It's monsoon season")
elif month.lower() in ['september', 'october', 'november']:
    # Post-monsoon months
    print("It's post-monsoon season")
else:
    # Handle invalid input
    print("Invalid month entered")
