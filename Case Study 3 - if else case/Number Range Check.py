#Write a Python program that checks if a given number lies within a certain range [10, 20].

n=int(input('Enter a number: ')) #Getting values from the user
r=range(10,20) #Setting range
if n in r: #Checking if the given number is in the range
  print('The number is in the range')
else:
  print('The number is not in the range')
