#Write a program that checks if a customer is eligible for a discount based on their purchase amount.

dis_amt=1200 #Setting discount applicable range
amt=int(input('Enter the total purchase amount: '))
if amt>=dis_amt: #Checking the condition
  print('Discount is applicable')
else:
  print('Discount is not applicable')
