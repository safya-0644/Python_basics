#Write a program that checks if a number is even or odd.

num=int(input('Enter a number: ')) #Getting value from the user
if num%2==0: #Checking condition (if the remainder when divided with 2 the it's even)
  print(f'{num} is an even number')
else: #or else odd
  print(f'{num} is a odd number')
