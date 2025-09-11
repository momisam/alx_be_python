#User Input for Financial Details:
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

#Calculate Monthly Savings:
monthly_savings = income - expenses
interest = 5 / 100
projected_savings = monthly_savings * 12 + int((monthly_savings * 12 * interest))



#Output 
print(f"Your monthly savings are ${monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")