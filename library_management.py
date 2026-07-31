class Book:
    def __init__(self,book_name,borrow_date,return_date,lender_name):
        self.book_name = book_name
        self.borrow_date = borrow_date
        self.return_date = return_date
        self.lender_name = lender_name
        
book1 = Book("Dear Debbie","01/07/26","08/07/26","Max")
print(book1.book_name)
print(book1.borrow_date)
print(book1.return_date)
print(book1.lender_name)
with open("borrowed books.txt",'w') as file:
    file.write("Book Name: " + book1.book_name + "\n")
    file.write("Borrow Date: " + book1.borrow_date + "\n")
    file.write("Return Date: " + book1.return_date + "\n")
    file.write("Lender Name: " + book1.lender_name + "\n")
book2 = Book("The night she disappeared","13/07/26","21/07/26", "Sophie")
print(book2.book_name)
print(book2.borrow_date)
print(book2.return_date)
print(book2.lender_name)
with open("borrowed books.txt",'a') as file:
    file.write("Book Name: " + book2.book_name + "\n")
    file.write("Borrow Date: " + book2.borrow_date + "\n")
    file.write("Return Date: " + book2.return_date + "\n")
    file.write("Lender Name: " + book2.lender_name + "\n")
with open("borrowed books.txt",'r') as file:
    print(file.read())
