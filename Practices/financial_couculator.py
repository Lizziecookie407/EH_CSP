#EH 6th Financial Calculator

print("Hi, welcome to my financial calculator! Put in each amount as a plain number.")

income = float(input("Your monthly income: "))
rent = float(input("Your monthly rent: "))
utilities = float(input("Your monthly utilities: "))
groceries = float(input("Your monthly groceries: "))
transportation = float(input("Your monthly transportation: "))
savings = income*.1
total_expenses = rent+utilities+groceries+transportation+savings #everything plus everything
spending = income-total_expenses #income - total

percent_savings = round(savings/income*100,0)
percent_rent = round(rent/income*100, 0)
percent_utilities = round(utilities/income*100,0)
percent_groceries = round(groceries/income*100,0)
percent_transportation = round(transportation/income*100,0)
percent_spending = round(spending/income*100,0)

print("\nYour rent is $", rent, "and that is", percent_rent, "% of your income.")
print("Your utilities are $", utilities, ", and that is", percent_utilities, "% of your income.")
print("Your groceries are $", groceries, ", and that is", percent_groceries, "% of your income.")
print("Your transportation is $", transportation, ", and that is", percent_transportation, "% of your income.")
print("You should save $", savings, "a month, and that is", percent_savings, "% of your income.")
print("You have $", spending, "of money left to spend each month, and that is",percent_spending, "% of your income.")
print("Thanks for using my calculator!")