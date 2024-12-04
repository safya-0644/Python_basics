#Print all prime numbers within a range

s = int(input('Enter the start range: '))  # Input for the start range
e = int(input('Enter the end range: '))  # Input for the end range
for i in range(s, e):  # Iterate over the numbers from s to e-1
    if i > 1:  # Prime numbers are greater than 1
        for j in range(2, i):  # Check divisibility from 2 to i-1
            if i % j == 0:  # If i is divisible by j, it's not prime
                break
        else:
            print(i)  # If no divisors are found, i is prime, so print it
