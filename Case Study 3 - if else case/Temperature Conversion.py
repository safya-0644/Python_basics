#Write a program that converts temperature from Celsius to Fahrenheit.

#Getting temperature from the user
c=int(input('Enter the temperature in celcius: '))
f=int(input('Enter the temperature in fahrenheit: '))

c_to_f=(c*9/5)+32 #Converting to fahrenheit
f_to_c=(f-32)*5/9 #Converting to celcius
print(f'{c} degree celcius is {c_to_f} fahrenheit')
print(f'{f} degree fahrenheit is {f_to_c} celcius')
