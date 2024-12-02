#Print first 10 natural numbers using while loop

i=int(input("Enter the start range: "))
n=int(input("Enter the end range: "))
while i<=n:
  print(i)
  i+=1

#Print the following pattern

for i in range(1,6):
  for j in range(1,i+1):
    print(j,end="")
  print()

#Calculate sum of all numbers from 1 to a given number

n=int(input('Enter a  number: '))
sum=0
for i in range(1,n+1):
  sum=sum+i
print(sum)

#Print multiplication table of a given number

n=int(input('Enter a number: '))
t=int(input('Enter the range value: '))
for i in range(1,t+1):
  mul=n*i
  print(mul)

#Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
  if num%5==0:
    if num>150:
      continue
    elif num>500:
      break
    print(num)

#Count the total number of digits in a number

n=int(input('Enter a number: '))
count=0
while n!=0:
  n=n//10
  count=count+1
print(count)

#Print the following pattern

for i in range(6,0,-1):
  for j in range(i,0,-1):
    print(j,end='')
  print()

#Print list in reverse order using a loop

l1=[10,20,30,40,50]
for i in range(len(l1)-1,-1,-1):
  print(l1[i])

#Display numbers from -10 to -1 using for loop

for i in range(-10,0):
  print(i)

#Display a message “Done” after the successful execution of the for loop

for i in range(5):
  print(i)
else:
  print('Done!')

#Print all prime numbers within a range

s=int(input('Enter the start range: '))
e=int(input('Enter the end range: '))
for i in range(s,e):
    if i>1:
        for j in range (2,i):
            if i%j==0:
                break
        else:
            print(i)

#Display Fibonacci series up to 10 terms

n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    for i in range (n):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
        count += 1

#Find the factorial of a given number

n=int(input('Enter a number: '))
fact=1
for i in range(1,n+1):
  fact=fact*i
print(fact)

#Reverse a integer number

n= int(input('Enter the integer: '))
rev=0
for i in range(n):
  if n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print(rev)

#Print elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(my_list[1::2])

(or)

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(len(my_list)):
  if i%2!=0:
    print(my_list[i])

#Calculate the cube of all numbers from 1 to a given number

n=int(input('Enter the values of starting range: '))
for i in range(1,n+1):
  print(f 'Current number is : {i} and the cube is : {i**3}')

#Find the sum of the series up to n terms

n= int(input('Enter the terms: '))
sum=0
for i in range(1,n+1):
  sum=sum+int('2'*i)
print(sum)

#Print the following pattern

for i in range(4):
  for j in range(i+1):
    print('*',end=' ')
  print()
for i in range(5):
  for j in range(i-1,4):
    print('*',end=' ')
  print()

(or)

for i in range(1, 5):
  print(' '.join(['*'] * i))  # Prints upward triangle

for i in range(5, 0, -1):
  print(' '.join(['*'] * i))  # Prints downward triangle

Output:

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
