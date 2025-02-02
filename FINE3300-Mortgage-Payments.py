
# 1: Calculates payments for different time periods
def mortgagePayments(principal, rate, amortization):
    # Rates for periods
    r_monthly = (1+rate/2)**(2/12) - 1
    r_semimonthly = (1+rate/2)**(2/24) - 1
    r_biweekly = (1+rate/2)**(2/26) - 1
    r_weekly = (1+rate/2)**(2/52) - 1

    # Payments for periods
    payment_monthly = (principal/((1-(1+r_monthly)**(-amortization*12))/r_monthly))
    payment_semimonthly = (principal/((1-(1+r_semimonthly)**(-amortization*24))/r_semimonthly))
    payment_biweekly = (principal/((1-(1+r_biweekly)**(-amortization*26))/r_biweekly))
    payment_weekly = (principal/((1-(1+r_weekly)**(-amortization*52))/r_weekly))
    payment_rapid_biweekly = payment_monthly / 2
    payment_rapid_weekly = payment_monthly / 4

    return (payment_monthly, payment_semimonthly, payment_biweekly, payment_weekly, payment_rapid_biweekly, payment_rapid_weekly)

# 2: get inputs from the user
principal_input = input("Please input the principal amount\n")
rate_input = input("Please input the interest rate\n")
amortization_input = input("Please input the amortization period\n")


# converts the input from a string to a integer/float
principal_input = int(principal_input)
rate_input = float(rate_input) / 100
amortization_input = int(amortization_input)

# run the function to get the payment amounts
result = mortgagePayments(principal_input, rate_input, amortization_input)

# 3: prints all the payments for different time periods
print("\nMonthly Payment: $" + str(round(result[0], 2)))
print("Semi-monthly Payment: $" + str(round(result[1], 2)))
print("Bi-weekly Payment: $" + str(round(result[2], 2)))
print("Weekly Payment: $" + str(round(result[3], 2)))
print("Rapid Bi-weekly Payment: $" + str(round(result[4], 2)))
print("Rapid weekly Payment: $" + str(round(result[5], 2)))










