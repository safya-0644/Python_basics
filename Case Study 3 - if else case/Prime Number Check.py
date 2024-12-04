#Write a program that checks if a number is prime.

num=int(input('Enter a number: ')) #Getting the values from the user
if num>1: #Checking if the value is positive
  for i in range(2,num):
    if num%i==0: #Checking if the number is prime 
      print("It's not a prime number")
      break
  else:
    print("It's a prime number")
else:
  print("It's not a prime number")
