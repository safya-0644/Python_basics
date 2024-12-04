#Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Othe20rwise, return their sum.

# Initialize two variables with given values
a = 20
b = 30

# Calculate the product of the two numbers
pro = a * b

# Check if the product is less than or equal to 1000
if pro <= 1000:
    # If the condition is true, print the product
    print(pro)
else:
    # Otherwise, print the sum of the two numbers
    print(a + b)
