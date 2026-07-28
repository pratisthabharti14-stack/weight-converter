print("Type of expenses:")
types = ["1)Accomodation", "2)Food", "3)Travel", "4)Extra"]

for type in types:
    print(type)

total = 0

for i in range(4):
    expense_type = input("Enter type of expense (1-4): ")

    if expense_type == '1':
        rent = float(input("Enter your monthly rent: "))
        water = float(input("Enter your estimated monthly water bill: "))
        electricity = float(input("Enter your estimated monthly electricity bill: "))

        total += rent + water + electricity
        print("Total expenses:", total)

    elif expense_type == '2':
        food = float(input("Enter your monthly food expenses: "))

        total += food
        print("Total expenses:", total)

    elif expense_type == '3':
        travel = float(input("Enter your monthly travel expenses: "))

        total += travel
        print("Total expenses:", total)

    elif expense_type == '4':
        extra = float(input("Enter extra monthly expenses: "))

        total += extra
        print("Total expenses:", total)

    else:
        print("Invalid choice")
print("Total monthly expenses:",total)
budget = float(input("Enter your monthly budget: "))
savings = budget - total
print("Total monthly savings:",savings)
if total > budget:
   print("Your total monthly expense is more than your total monthly budget")
   print("Your total monthly expense is greater than budget by:", total - budget)
else:
   print("You have ₹", savings,"left from your budget")