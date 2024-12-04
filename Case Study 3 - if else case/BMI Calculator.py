#Write a program that calculates the Body Mass Index (BMI) and categorizes it.

weight=float(input('Enter your weight in kg: ')) #Getting weight 
height=float(input('Enter your height in m: ')) #Getting height 
bmi=weight/(height**2) #Calculating the BMI
print('The BMI value is: ',bmi)
