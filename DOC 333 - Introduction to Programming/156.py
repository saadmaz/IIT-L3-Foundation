# Input gross salary
gross_sal = float(input("Enter monthly salary: "))

# Initialize tax percentages
tax_perc1 = 0.0
tax_perc2 = 0.05
tax_perc3 = 0.10
tax_perc4 = 0.12

# Initialize tax amounts for each bracket
tax_amount1 = 0.0
tax_amount2 = 0.0
tax_amount3 = 0.0
tax_amount4 = 0.0

# Calculate tax for the first 99,999 units
if gross_sal > 99999:
    if gross_sal <= 199999:
        tax_amount1 = (gross_sal - 99999) * tax_perc1
    else:
        tax_amount1 = (199999 - 99999) * tax_perc1
        tax_amount2 = (gross_sal - 199999) * tax_perc2

# Calculate tax for the next 50,000 units
elif gross_sal > 149999:
    tax_amount2 = (gross_sal - 149999) * tax_perc2

# Calculate tax for the next 100,000 units
elif gross_sal > 249999:
    tax_amount3 = (gross_sal - 249999) * tax_perc3

# Calculate tax for any remaining units above 250,000
else:
    tax_amount4 = gross_sal * tax_perc4

# Calculate total tax amount
tot_tax_amount = tax_amount1 + tax_amount2 + tax_amount3 + tax_amount4

# Calculate net salary
net_sal = gross_sal - tot_tax_amount

# Print net salary
print(f"Your monthly net salary is: {net_sal:.2f}")
