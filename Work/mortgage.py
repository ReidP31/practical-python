# mortgage.py
#
# Exercise 1.7

# set mortgage variables
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

# set variables for first year payment plan
first_year_payment = payment + 1000
first_year_paid = 0.0

# create first year loop to calculate a) principal for first year and b) total paid for first year
for month in range(1,13):
    principal = principal * (1+rate/12) - first_year_payment
    first_year_paid += first_year_payment

# initialize months variable for counting number of months a payment is made
months = 0

# set loop for decrementing principal amount by monthly payment amount until principal is paid
while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    months += 1

# print total paid amount and number of months a payment is made
print(f'Total paid: {round(total_paid + first_year_paid, 2)}')
print(f'Total months: {months + month}')