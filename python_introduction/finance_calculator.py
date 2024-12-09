# Function to calculate monthly and yearly savings  
def calculate_savings():  
    # User Input for Financial Details  
    monthly_income = float(input("Enter your monthly income: "))  
    total_expenses = float(input("Enter your total monthly expenses: "))  

    # Calculate Monthly Savings  
    monthly_savings = monthly_income - total_expenses  

    # Project Annual Savings  
    interest_rate = 0.05  # 5% interest rate  
    projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate)  

    # Output Results  
    print(f"Your monthly savings are ${monthly_savings:.2f}.")  
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")  

# Run the savings calculation  
calculate_savings()
