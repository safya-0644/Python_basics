#Write a program that checks if a student is admitted based on their test score.

admission_test_score=50 #Setting the margin score for admission
st_ad_det=[]
while True:
  data=input('Enter Student name and last year mark: ') #Getting the student details
  if data=='':
    break
  data=data.split(',') #Seperating the values next to ,

  #Assining values based on index values
  s_name=data[0]
  mark=int(data[1])

  #Checking if the admission condition is met
  if mark>=admission_test_score:
    result='Admitted'
  else:
    result='Not Admitted'

  #Updating the values
  st_ad_det.append([s_name,mark,result])
#Printing the final values
print('Final details: ')
for detail in st_ad_det:
  print(detail)
