#Write a Python program to calculate the BMI (Body Mass Index) and categorize it.

# Get weight and height input from the user
weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in m: '))

# Calculate BMI using the formula
bmi = weight / (height ** 2)

# Determine BMI category based on the calculated value
if bmi < 18.5:
    # BMI below 18.5 is considered underweight
    print('Underweight')
elif 18.5 <= bmi <= 25:
    # BMI between 18.5 and 25 is considered normal
    print('Normal')
elif 25 < bmi <= 30:
    # BMI between 25 and 30 is considered overweight
    print('Overweight')
else:
    # BMI above 30 is considered obese
    print('Obesity')
