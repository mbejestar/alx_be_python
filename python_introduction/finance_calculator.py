# Prompt the user for their monthly income
monthly_income = float(input("Enter your monthly income: "))

# Ask for their total monthly expenses
total_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - total_expenses

# Assume a simple annual interest rate of 5%
annual_interest_rate = 0.05

# Projct annual savings including interest
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# Print the result
print(f"Your projected savings after one year, including interest, will be: ${projected_savings:.2f}")
