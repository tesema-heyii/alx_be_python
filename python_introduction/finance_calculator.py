annual_interest_rate = 0.05
time = 12 # in months
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
print("Your monthly savings are $",monthly_savings)
print("Projected savings after one year, with interest, is: $",(monthly_savings*12) + (monthly_savings*12*annual_interest_rate))
# lets check this one if there is something new and lets continue to the next one lets go and do it here in the bellow