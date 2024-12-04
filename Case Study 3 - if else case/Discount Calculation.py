#Write a program that calculates the final price after applying a discount.

discount_details=[] #Creating a list
while True:
  data=input('Enter the details (Product,actual_price,discount): ') #Gettin data from user
  if data=='':
    break
  data=data.split(',') #Seperating the values
  #Assigning index values to the variables
  product=data[0] 
  actual_price=int(data[1])
  discount=int(data[2])

  #Calculating price after discount
  dis=(actual_price/100)*discount
  final_price=actual_price-dis

  #Adding the calculated values to the list discount_det
  discount_details.append([product,actual_price,discount,final_price])

#Displaying the final values
print('Final details: ')
for detail in discount_details:
  print(detail)
