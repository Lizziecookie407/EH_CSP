#EH 6th Updated Financial Calculator

print("Hi, welcome to my financial calculator! Put in each amount as a plain number.")

def input_amount(amount):
    return float(input(f"Your monthly {amount}: "))
    

def percent_amount(amount):
    round(amount/income*100,0)

income= input_amount("income")
rent= input_amount("rent")
utilities = input_amount("utilities")
groceries = input_amount("groceries")
transportation = input_amount("transportation")
savings= income*.1
total_expenses = rent+utilities+groceries+transportation+savings
spending = income-total_expenses

percent_savings = percent_amount("savings")
percent_rent = percent_amount("rent")
percent_utilities = percent_amount("utilities")
percent_groceries = percent_amount("groceries")
percent_transportation = percent_amount("transportation")
percent_spending = percent_amount("spending")