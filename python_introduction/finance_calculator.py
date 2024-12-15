# finance_calculator.py  

# Prompt the user for their financial data  
monthly_income = float(input("Enter your monthly income: "))  
monthly_expenses = float(input("Enter your total monthly expenses: "))  

# Calculate the monthly savings  
monthly_savings = monthly_income - monthly_expenses  

# Define the annual interest rate  
annual_interest_rate = 0.05  

# Calculate the projected savings after one year  
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)  

# Display the results  
print("Your monthly savings are ${:.2f}.".format(monthly_savings))  
print("Projected savings after one year, with interest, is: ${:.2f}.".format(projected_savings))