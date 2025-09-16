#EH 6th Updated Financial Calculator

print("Hi, welcome to my financial calculator! Put in each amount as a plain number.")

def input_amount(amount):
    return float(input(f"Your monthly {amount}: "))

def percent_amount(amount):
    return round(amount/income*100,0)

income= input_amount("income")
rent= input_amount("rent")
utilities = input_amount("utilities")
groceries = input_amount("groceries")
transportation = input_amount("transportation")
savings= income*.1
total_expenses = rent+utilities+groceries+transportation+savings
spending = income-total_expenses

percent_savings = percent_amount(savings)
percent_rent = percent_amount(rent)
percent_utilities = percent_amount(utilities)
percent_groceries = percent_amount(groceries)
percent_transportation = percent_amount(transportation)
percent_spending = percent_amount(spending)

print("\nYour rent is $", rent, "and that is", percent_rent, "% of your income.")
print("Your utilities are $", utilities, ", and that is", percent_utilities, "% of your income.")
print("Your groceries are $", groceries, ", and that is", percent_groceries, "% of your income.")
print("Your transportation is $", transportation, ", and that is", percent_transportation, "% of your income.")
print("You should save $", savings, "a month, and that is", percent_savings, "% of your income.")
print("You have $", spending, "of money left to spend each month, and that is",percent_spending, "% of your income.")
print("Thanks for using my calculator!")