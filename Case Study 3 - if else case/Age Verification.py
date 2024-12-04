#Write a program that checks if a person is eligible to vote.

#Getting values from the user
data = input("Enter student details (Name,Age) separated by semicolons: ")
pep_det = []
people = data.split(';')  
for person in people:
    #Seperating values next to ,
    people_det = person.split(',')
    name = people_det[0]
    age = int(people_det[1])
    #Checking age condition
    if age >=18:
        eligibility = 'Eligible'
    else:
        eligibility = 'Not Eligible'
    #Updating the values
    pep_det.append([name, age , eligibility])
#Print all the values
print("\nFinal details:")
for person in pep_det:
    print(person)

