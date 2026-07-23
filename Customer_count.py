class Customer: 
     customer_count = 0
     def__init__(self,name,order,token_number):
                 self.name = name
                 self.order = order  
                 self.token_number = token_number
                Customer.customer_count += 1
    def display_customer(self):
                print(f"Customer_Name:              {self.name},Order:{self.order},Token_Number:  {self.token_number}")
 
customer1 = Customer("Max","Bulgogi","14")

customer1.display_customer()

customer2 = Customer("Bruce","Bibimbap","15")

customer2.display_customer ()

customer3 = Customer("Mary","Kalguksu","16")

customer3.display_customer()

print(f"Total Customers:{Customer.customer_count}")