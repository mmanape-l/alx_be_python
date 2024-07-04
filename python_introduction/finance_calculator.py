# finance_calculator.py
def main():
    # Prompt the user for their monthly income
    monthly_income = float(input("Enter your monthly income: "))
    # Ask for their total monthly expenses
    monthly_expenses = float(input("Enter your total monthly expenses: "))
    # Calculate the monthly savings
    monthly_savings = monthly_income - monthly_expenses
    # Assume a simple annual interest rate of 5%
    annual_interest_rate = 0.05
    # Project annual savings incorporating the interest
    annual_savings = monthly_savings * 12
    projected_savings = annual_savings + (annual_savings * annual_interest_rate)
    # Print the calculated results
    print(f"Your monthly savings are: {monthly_savings}")
    print(f"Your projected annual savings after one year, including interest, are: {projected_savings}")
# Entry point of the script
if __name__ == "__main__":
    main()