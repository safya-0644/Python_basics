# Define two lists of numbers
l1 = [10, 20, 25, 30, 35]
l2 = [40, 45, 60, 75, 90]

# Initialize an empty list to store the filtered numbers
newl1 = []

# Loop through the first list and append odd numbers to newl1
for i in l1:
    if i % 2 != 0:
        newl1.append(i)

# Loop through the second list and append even numbers to newl1
for j in l2:
    if j % 2 == 0:
        newl1.append(j)

# Print the result containing odd numbers from l1 and even numbers from l2
print('Result: ', newl1)
