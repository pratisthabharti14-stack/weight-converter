class Expense:
    all_expenses = []
    def __init__(self,name, category,amount):
        self.name = name
        self.category = category 
        self.amount = amount 
    def show_details(self):
        print("\n Expense Details:")
        print(f"Name:{self.name}")
        print(f"Category:{self.category}")
        print(f"Amount:{self.amount}")
    @classmethod
    def add_expense(cls):
        name = input("Enter the name of expense: ")
        category = input("Enter the type of expense: ")
        while True:
            try:
                amount = float(input("Enter the amount: "))
                break
            except ValueError:
                 print("Invalid amount! Please enter a number.")
        
        expense = Expense(name, category, amount)
        cls.all_expenses.append(expense)
        print(f"Expense: {amount} of type: {category} added successfully")
    @classmethod
    def view_expense(cls):
        if not cls.all_expenses:
             print("No expense found!")
        else:
            for expense in cls.all_expenses:
                expense.show_details()
    @classmethod
    def delete_expense(cls):
        if not cls.all_expenses:
             print("No expense found!")
             return
        name = input("Enter the name of the expense you want to delete: ")

        for expense in cls.all_expenses:
            if expense.name.lower() == name.lower():
                cls.all_expenses.remove(expense)
                print(f"{expense.name} deleted successfully!")
                return
        print("Expense not found!")
    @classmethod
    def total_expense(cls):
        if not cls.all_expenses:
            print("No expense found")
            return
        total = 0 
        for expense in cls.all_expenses:
            total += expense.amount
        print(f"Total expenses: {total}")

    
def menu():
    while True:
        print("\n ========Expenses========")
        print("1.Add Expense")
        print("2.Show Expenses")
        print("3.Delete an expense")
        print("4.View Total Expenses")
        print("5.Exit")
        choice = input("Enter your choice(1-5): ")
        if choice == '1':
            Expense.add_expense()
        elif choice == '2':
            Expense.view_expense()
        elif choice == '3':
            Expense.delete_expense()
        elif choice == '4':
            Expense.total_expense()
        elif choice =='5':
            print("Exiting the program, Goodbye!")
            break
        else:
            print("Invaild choice, Try again!")
if __name__ == '__main__':
    menu()