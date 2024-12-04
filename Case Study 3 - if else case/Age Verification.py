#Write a program that checks if a person is eligible to vote.
data = input("Enter student details (Name,Age) separated by semicolons: ")
pep_det = []
people = data.split(';')  
for person in people:
    people_det = person.split(',')
    name = people_det[0]
    age = int(people_det[1])
    
    if age >=18:
        eligibility = 'Eligible'
    else:
        eligibility = 'Not Eligible'
    
    pep_det.append([name, age , eligibility])

print("\nFinal details:")
for person in pep_det:
    print(person)

