# Saving, with a raise

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04

value_down_payment = total_cost*portion_down_payment
months_spend = 0
while(current_savings < value_down_payment):
  return_of_investments = current_savings*(r/12)
  saved_this_month = (annual_salary/12)*portion_saved
  months_spend += 1
  current_savings += return_of_investments + saved_this_month
  if months_spend%6 == 0:
    annual_salary = annual_salary*(1+semi_annual_raise)

print("Number of months:", months_spend)

150000
0.441
1000000
0.07