# Assignment 1
print("50 + 50 = " + str(50 + 50), "100 - 10 = " + str(100-10))

# Assignment 2
# print("30+*6,6^6,6**6,6+6+6+6+6+6 = " + str(30+*6,6^6,6**6,6+6+6+6+6+6))

# Assignment 3
print("Hello World")
print("Hello World : 10")

# Assignment 4 (MORTGAGE CALCULATOR)

def mortgage_calculator(loan_amount, interest, months):
    interest_rate = interest / 100 / 12
    monthly_payment = loan_amount * (interest_rate * (1 + interest_rate) ** months) / ((1 + interest_rate) ** months - 1)
    print("The required monthly payment is: " + str(round(monthly_payment)))

mortgage_calculator(800000, 6, 103)