#Write a Python program to calculate the grade of a student based on their marks.

# Get the student's mark from user input
mark = int(input('Enter your mark: '))

# Determine the grade based on the mark
if mark > 450:
    # Marks above 450 receive A1 Grade
    print('A1 Grade')
elif 400 <= mark <= 450:
    # Marks between 400 and 450 receive A Grade
    print('A Grade')
elif 350 <= mark < 400:
    # Marks between 350 and 399 receive B Grade
    print('B Grade')
elif 300 <= mark < 350:
    # Marks between 300 and 349 receive C Grade
    print('C Grade')
elif 250 <= mark < 300:
    # Marks between 250 and 299 receive D Grade
    print('D Grade')
else:
    # Marks below 250 receive E Grade
    print('E Grade')
