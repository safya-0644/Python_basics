'''Calculate the multiplication and sum of two numbers
Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Othe20rwise, return their sum.'''

a=20
b=30
pro=a*b
if pro<=1000:
  print(pro)
else:
  print(a+b)

#Print the Sum of a Current Number and a Previous number.

n1=int(input('Enter the values of starting range: '))
n2=int(input('Enter the values of ending range: '))
for i in range(n1,n2):
  print(f 'Current number {i} previous number {i-1} sum:{i+i-1}')

#Print characters present at an even index number

str=input('Enter a string value: ')
s=len(str)
n=9
if n<s:
  print(str[::n])
else:
  print('Invalid')

(or)

str=input('Enter a string value: ')
s=len(str)
for i in range(s):
  if i%2==0:
    print(str[i])

#Remove first n characters from a string

str=input('Enter a string:')
n=int(input('Enter the no.of.first char to be removed: '))
print(str[n:])

#Check if the first and last numbers of a list are the same

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
x1=numbers_x[0]
x2=numbers_x[-1]
y1=numbers_y[0]
y2=numbers_y[-1]
print(numbers_x)
if x1==x2:
  print('Result is True')
else:
  print('Result is False')
print (numbers_y)
if y1==y2:
  print('Result is True')
else:
  print('Result is False')
  
#Display numbers divisible by 5

l=[10, 20, 33, 46, 55]
for i in l:
  if i%5==0:
    print(i)

#Find the number of occurrences of a substring in a string

str_x="Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))

#Print the following pattern

row=5
for i in range(1,row+1):
  for j in range(1,i+1):
    print(i,end=' ')
  print()

#Check Palindrome Number

str_a=input('Enter a value: ')
if str_a==str_a[::-1]:
  print('Yes, given number is a palindrome')
else:
  print('No, given number is not a palindrome')

#Merge two lists using the following condition

l1 = [10, 20, 25, 30, 35]
l2 = [40, 45, 60, 75, 90]
newl1=[]
for i in l1:
  if i%2!=0:
    newl1.append(i)
for j in l2:
  if j%2==0:
    newl1.append(j)
print('Result: ',newl1)

#Get each digit from a number in the reverse order.

num=(input("Enter a number:"))
print(' '.join(num[::-1]))

#Calculate income tax

income = int(input("Enter a income:"))
if income <= 10000:
  tax = 0
elif income <= 20000:
  tax = (income - 10000) * 10 / 100
else:
  tax = (income - 20000) * 20 / 100 + 10000 * 0.1
print(f 'Total tax to pay is {tax}')

#Print multiplication table from 1 to 10

for i in range (1,11):
  for j in range (1,11):
    j=i*j
    print(j,end=' ')
  print()

#Print a downward half-pyramid pattern of stars

for i in range(6):
  for j in range(i-1,5):
    print('*',end=' ')
  print()

#Get an int value of base raises to the power of exponent

b=int(input('Enter the base values: '))
e=int(input('Enter the exponent values: '))
print(f'{b} raises to the power of {e}:',b**e)
