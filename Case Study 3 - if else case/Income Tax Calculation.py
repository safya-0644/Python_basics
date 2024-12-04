#Write a Python program to calculate the income tax based on given slabs.
#if the income is less than 10,000 then no tax to be paid.
#if the income is greater than 10,000 and less than 20,000 then 10% of income to be paid as tax.
#if the income is greater than 20,000 then 20% of income to be paid as tax.
income=int(input('Enter the total income: '))
if income<=10000:
  tax=0
elif income<=20000:
  tax=(income-10000)*(10/100)
else:
  tax=(income-20000)*(20/100)+(10000*0.1)
print(f 'The tax amount is {tax}')
