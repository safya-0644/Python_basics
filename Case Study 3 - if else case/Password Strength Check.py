#Write a Python program to check the strength of a password. It should have at least 8 characters, include at least one number, and at least one uppercase letter.

import re 
password=input('Enter your password:')
#Checking if it have at least 8 characters, at least one uppercase letter, at least one special character, include at least one number.
if len(password)>=8 and re.search('[a-z]',password) and re.search('[A-Z]',password) and re.search('[@_$]', password):
  print('Valid password')
else:
  print('Invalid password')
