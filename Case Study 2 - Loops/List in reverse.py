#Print list in reverse order using a loop

l1 = [10, 20, 30, 40, 50]  # List of numbers
for i in range(len(l1)-1, -1, -1):  # Loop starts from the last index and moves backwards
    print(l1[i])  # Print the element at the current index
