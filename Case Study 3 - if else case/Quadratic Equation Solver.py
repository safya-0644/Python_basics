#Write a Python program that solves quadratic equations (ax^2 + bx + c = 0) and displays the roots.

import cmath #importing cmath library for square root 

#Getting values for the variables a,b,c
a=int(input('Enter a: '))
b=int(input('Enter b: '))
c=int(input('Enter c: '))

#Calculating the quadratic formula
d=(b**2)-(4*a*c)
sol1=(-b - cmath.sqrt(d))/2*a
sol2=(-b + cmath.sqrt(d))/2*a
#Printing the solution
print(f 'The solution are {sol1:.2f} and {sol2:.2f}')
