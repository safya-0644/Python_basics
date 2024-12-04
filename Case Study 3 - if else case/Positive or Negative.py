#Write a program that checks if a number is positive, negative, or zero.

num=int(input('Enter a number: ')) #Getting value from the user
if num==0: #Checking if the given number is equal to 0
  print('The given number is zero')
elif num>0: #if the number is greater than 1 then it's positive
  print('The given number is positive')
else: #or else it's negative number
  print('The given number is negative')
