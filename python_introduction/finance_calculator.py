# Get user input for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Get user input for total monthly expenses
total_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - total_expenses

# Assume annual interest rate of 5%
annual_interest_rate = 0.05

# Calculate total savings after one year (without interest)
total_savings = monthly_savings * 12

# Calculate earned interest for one year
earned_interest = total_savings * annual_interest_rate

# Calculate total projected savings (savings + interest)
projected_savings = total_savings + earned_interest

# Print the final projected savings
print(f"Your projected savings after one year, including interest, will be: ${projected_savings:.2f}")
