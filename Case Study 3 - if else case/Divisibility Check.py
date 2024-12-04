#Write a Python program that checks if a number is divisible by 3, 5, or both.

#Getting values from the user
num=int(input('Enter a number: ’)) 
if num%3==0 and num%5==0:  #Checking divisible by both 3&5
  print('The number is divisible by both 3&5')
elif num%3==0: #or checking divisible by 3
  print('The number is divisible by 3 only')
elif num%5==0: #or checking divisible by 5
  print('The number is divisible by 5 only')
else:
  print('The number, neither divisible by 5 nor by 3')
