print("-----Welcome to the SIT Tax Calculator------")
salary = (float(input("Enter your salary to calculate tax:")))

if salary < 30000:
    tax_amount = salary * 0.05
elif 30000 <= salary <= 70000:
    tax_amount = salary * 0.15
else:
    tax_amount = salary * 0.25

print("Your tax is: ", tax_amount)


