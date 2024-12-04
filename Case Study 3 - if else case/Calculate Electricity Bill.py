#Write a Python program to calculate the electricity bill based on the following rates:
# Get the number of units consumed from the user
units = int(input('Enter the unit: '))

# Calculate the bill based on the units consumed
if units <= 100:
    # For the first 100 units, the rate is rs.10 per unit
    bill = units * 10
elif 100 < units <= 200:
    # For units between 101 and 200, the rate is rs.15 per unit
    bill = (100 * 10) + (units - 100) * 15
elif 200 < units <= 300:
    # For units between 201 and 300, the rate is rs.20 per unit
    bill = (100 * 10) + (100 * 15) + (units - 200) * 20
else:
    # For units above 300, the rate is rs.25 per unit
    bill = (100 * 10) + (100 * 15) + (100 * 20) + (units - 300) * 25

# Print the calculated bill amount
print(f'The bill amount is {bill}')
