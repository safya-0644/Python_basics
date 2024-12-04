#Print first 10 natural numbers using while loop

# Taking the start and end values as input
i = int(input("Enter the start range: "))  # The starting value
n = int(input("Enter the end range: "))  # The ending value

# Loop to print numbers from i to n (inclusive)
while i <= n:
    print(i)
    i += 1  # Increment the value of i after each iteration
