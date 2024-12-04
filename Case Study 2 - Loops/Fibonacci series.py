#Display Fibonacci series up to 10 terms

n = int(input("Enter the number of terms: "))  # Input for the number of terms in the Fibonacci sequence
a, b = 0, 1  # The first two terms of the Fibonacci sequence (0 and 1)
count = 0  # A counter to keep track of the number of terms printed

if n <= 0:  # If the input is zero or negative
    print("Please enter a positive integer.")
elif n == 1:  # If the user requests only the first term of the sequence
    print("Fibonacci sequence:")
    print(a)  # Print the first term, which is 0
else:  # For n greater than 1
    print("Fibonacci sequence:")
    for i in range(n):  # Loop to print the Fibonacci sequence up to n terms
        print(a, end=" ")  # Print the current term
        temp = a + b  # Calculate the next term by adding the last two terms
        a = b  # Update a to be the last term
        b = temp  # Update b to be the new term
        count += 1  # Increment the counter (though it's not really used after the loop)
