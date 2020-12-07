
# User Input
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# conversions
monthly_salary = annual_salary / 12
print('monthly salary is', monthly_salary)

portion_down_payment = .25

r = .04

down_payment_cost = total_cost - (total_cost * portion_down_payment)

adjusted_savings = (monthly_salary * portion_saved * r) + (portion_saved * monthly_salary)

# Loop
current_savings = 0
number_of_months = 0

while current_savings < down_payment_cost:
    current_savings += adjusted_savings
    number_of_months += 1

print('Number of months: ', number_of_months) 
print('Savings amount ', current_savings)
