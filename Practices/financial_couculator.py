#EH 6th Financial Calculator
#save money as float rounded to two decimals

income = 3000
rent = 1200
utilities = 250
groceries = 200
transportation = 500

savings = 300 #10 percent
percent_rent = 1200/300
total_expenses= 9 #rent +  #everything plus everything 
spending = 9 #income - total

income = float(input("Your monthly income: "))
rent = float(input("Your monthly rent: "))
utilities = float(input("Your monthly utilities: "))
goceries = float(input("Your monthly groceries: "))
transportation = float(input("Your monthly transportation: "))

print("\n\nIncome:",income)
print("\nRent:",rent,",",percent_rent)