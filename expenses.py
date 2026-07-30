while True:
    print("\n1.Add Expense")
    print("2.View Expenses")
    print ("3.Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        expense = input("Enter your Expense: ₹")
        with open("expenses.txt","a") as file:
           file.write(expense + "\n")
        print("Expense added successfully")
    elif choice == '2':
        with open("expenses.txt","r") as file:
           expenses = file.read()
        print("\nYour expenses:")
        print(expenses)
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
