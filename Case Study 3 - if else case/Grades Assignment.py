#Write a program that assigns grades to students based on their scores.

#Giving values (Values already assigned)
st_det=[[1,'Aron',98],[2,'Boston',72],[2,'Charles',65],
 [4,'David',43],[5,'Edward',21]]

for student in st_det:
 #Assigning values in the 2nd index as marks
  mark=student[2]

 #Calculating grades
  if mark>90:
    grade='A'
  elif mark>80 and mark<=90:
    grade='B'
  elif mark>70 and mark<=80:
    grade='C'
  elif mark>60 and mark<=70:
    grade='D'
  else:
    grade='E'

 #Storing updated values in the list
  student.append(grade)

#Printing individual students 
for student in st_det:
  print(student)
#----------------------------------------------------------------------------------------------------
#(or)

st_det=[]
n=int(input('Enter number of students: '))
for i in range(n):
 
#Getting values from the user seperately
  st_id=int(input('Enter student id: '))
  st_name=input('Enter student name: ')
  st_mark=int(input('Enter student mark: '))

 #Calculating grades
  if st_mark>90:
    grade='A'
  elif st_mark>80 and mark<=90:
    grade='B'
  elif st_mark>70 and mark<=80:
    grade='C'
  elif st_mark>60 and mark<=70:
    grade='D'
  else:
    grade='E'

 #Storing updated values in the list
  st_det.append([st_id,st_name,st_mark,grade])
#Printing individual students 
print('Final students details: ')
for student in st_det:
  print(student)

#-----------------------------------------------------------------------------------------------------
#(or)

#Getting individual student's value at once
data = input("Enter student details (ID,Name,Marks) separated by semicolons: ")
st_det = []
students = data.split(';')  
for student in students:

 #Assigning values according to it's index value
    student_data = student.split(',')
    student_id = int(student_data[0])
    name = student_data[1]
    marks = int(student_data[2])

 #Calculating grades
    if marks > 90:
        grade = 'Grade A'
    elif 80 < marks <= 90:
        grade = 'Grade B'
    elif 70 < marks <= 80:
        grade = 'Grade C'
    elif 60 < marks <= 70:
        grade = 'Grade D'
    else:
        grade = 'Grade E'
     
    #Storing updated values in the list
    st_det.append([student_id, name, marks, grade])
#Printing individual students 
print("\nFinal student details with grades:")
for student in st_det:
    print(student)

