#Write a Python program to check whether a triangle is valid or not given its three sides.

side=input('Enter the sides with comma: ') #Getting values from the user
side=side.split(',') #Seperating the values next to ,
s_count=len(side) #Storing the length of the value
if s_count==3: #If the count is 3 then it's a triangle
  print('It is a triangle')
else: #or else not a triangle
  print('It is not a triangle')
