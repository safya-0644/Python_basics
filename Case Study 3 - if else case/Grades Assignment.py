#Grades Assignment : 
#Write a program that assigns grades to students based on their scores.

st_det=[[1,'Aron',98],[2,'Boston',72],[2,'Charles',65],
 [4,'David',43],[5,'Edward',21]]

for student in st_det:
  mark=student[2]
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
  
  student.append(grade)

for student in st_det:
  print(student)

#(or)

st_det=[]
n=int(input('Enter number of students: '))
for i in range(n):
  st_id=int(input('Enter student id: '))
  st_name=input('Enter student name: ')
  st_mark=int(input('Enter student mark: '))
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
  st_det.append([st_id,st_name,st_mark,grade])

print('Final students details: ')
for student in st_det:
  print(student)

#(or)

data = input("Enter student details (ID,Name,Marks) separated by semicolons: ")
st_det = []
students = data.split(';')  
for student in students:
    student_data = student.split(',')
    student_id = int(student_data[0])
    name = student_data[1]
    marks = int(student_data[2])
    
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
    
    st_det.append([student_id, name, marks, grade])

print("\nFinal student details with grades:")
for student in st_det:
    print(student)

