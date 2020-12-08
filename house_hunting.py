
# User Input
annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
annual_rate = float(input('Enter the expected annual rate of return: ') or '.04')
total_cost = int(input('Enter the cost of your dream home: '))
down_payment = float(input('Enter the percent of your homes cost to save as a down payment: ') or '.25')

# conversions
monthly_salary = annual_salary / 12

portion_down_payment = down_payment
# portion_down_payment = .25

r = annual_rate
# r = .04

down_payment_cost = total_cost * portion_down_payment
print('down payment is', down_payment_cost)


# Loop
current_savings = 0
# annual_return = current_savings * r / 12
adjusted_savings = current_savings * portion_saved * r / 12
monthly_savings_deposit = monthly_salary * portion_saved
print('monthly deposit into savings is ', monthly_savings_deposit)
number_of_months = 0

while current_savings < down_payment_cost:
    current_savings = (current_savings + monthly_savings_deposit) + (1 + r / 12)
    number_of_months += 1
    print(current_savings)
print('Number of months ', number_of_months)


# while current_savings < down_payment_cost:
#     current_savings += monthly_savings_deposit
#     current_savings += adjusted_savings
#     number_of_months += 1
#     # print(number_of_months)
#     print(current_savings)
# years = number_of_months / 12
# print('Number of months: ', number_of_months)
# print('Number of years: ', number_of_months / 12)
# # print('compound interest is ', 1000(1 + .04 / 100) ** years)
# print('Savings amount ', current_savings)
