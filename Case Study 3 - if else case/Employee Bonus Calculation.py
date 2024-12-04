#Write a Python program that calculates the bonus for an employee based on their years of service.

# Initialize an empty list to store employee details
emp_det = []

# Continuously prompt the user for employee details until an empty input is given
while True:
    data = input("Enter employee's details (name, year of service, salary) or press Enter to stop: ")
    if data.strip() == '':  # Check for empty input
        break

    try:
        # Split and extract input values
        data = data.split(',')
        name = data[0].strip()  # Remove extra spaces if any
        year = int(data[1].strip())
        salary = int(data[2].strip())

        # Calculate bonus salary based on years of service
        if year > 10:
            bonus_salary = salary + salary * (10 / 100)
        elif 5 < year <= 10:
            bonus_salary = salary + salary * (5 / 100)
        else:
            bonus_salary = salary + salary * (2 / 100)

        # Append the employee's details to the list
        emp_det.append([name, year, salary, bonus_salary])

    except (IndexError, ValueError):
        # Handle invalid input format
        print("Invalid input! Please enter details in the format: name, year of service, salary")

# Display the employee details after bonus calculation
print("\nEmployee details after bonus calculation:")
print(f"{'Name':<15}{'Years of Service':<20}{'Salary':<15}{'Bonus Salary':<15}")
print("-" * 65)
for detail in emp_det:
    print(f"{detail[0]:<15}{detail[1]:<20}{detail[2]:<15}{detail[3]:<15.2f}")
