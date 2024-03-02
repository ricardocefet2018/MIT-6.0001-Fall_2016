# Finding the right amount to save away

annual_salary = float(input("Enter your annual salary: "))

semi_annual_raise = 0.07
r = 0.04
monthly_r = r/12
portion_down_payment = 0.25
total_cost = 1000000
value_down_payment = total_cost*portion_down_payment
current_savings = 0

month_num = 36
epslon = 100

high = 10000
low = 0

steps = 0
previous_portion_saved = 0
isPossibleToBuy = True
while (abs(current_savings - value_down_payment) > epslon):
  steps += 1
  current_savings = 0
  monthly_salary = annual_salary/12

  portion_saved = (high+low)//2

  for i in range(1, month_num+1):
    current_savings += current_savings * monthly_r
    current_savings += monthly_salary * (portion_saved/10000)
    if (i % 6 == 0):
      monthly_salary = monthly_salary * (1+semi_annual_raise)
  
  if current_savings < value_down_payment:
    low = portion_saved
  else:
    high = portion_saved
  
  if (previous_portion_saved == portion_saved):
    isPossibleToBuy = False
    break

  previous_portion_saved = portion_saved

if not isPossibleToBuy:
  print("It is not possible to pay the down payment in three years.")
else:
  print("Best savings rate:", portion_saved/10000)
  print("Steps in bisection search:", steps)