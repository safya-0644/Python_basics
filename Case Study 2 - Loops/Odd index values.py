#Print elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # List of elements
for i in range(len(my_list)):  # Loop through all indices of the list
    if i % 2 != 0:  # Check if the index is odd
        print(my_list[i])  # Print the element at the odd index
