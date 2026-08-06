class Book:
    all_books = []

    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.borrow_date = None
        self.return_date = None
        self.available = True

        Book.all_books.append(self)

    def show_details(self):
        print("\nBook details:")
        print(f"Title: {self.name}")
        print(f"Author: {self.author}")
        print(f"Date borrowed: {self.borrow_date}")
        print(f"Date returned: {self.return_date}")


    @classmethod
    def borrow_book(cls):
        member_id = int(input("Enter your member ID: "))

        selected_member = None

        for member in Member.all_members:
            if member_id == member.member_id:
                selected_member = member
                print(f"Welcome {member.name}")
                break

        if selected_member is None:
            print("Member not found")
            return

        name = input("Enter the title of book you want to borrow: ")
        date = input("Enter the date on which the book is being borrowed: ")

        for book in cls.all_books:
            if name == book.name.lower:

                if book.available:
                    book.borrow_date = date
                    book.available = False

                    selected_member.borrowed_books.append(book)

                    print(f"The book '{book.name}' has been borrowed by {selected_member.name}")

                else:
                    print("The book is already borrowed")

                return

        print("Book not found")


    @classmethod
    def return_book(cls):
        member_id = int(input("Enter your member ID: "))

        selected_member = None

        for member in Member.all_members:
            if member_id == member.member_id:
                selected_member = member
                print(f"Welcome {member.name}")
                break

        if selected_member is None:
            print("Member not found")
            return

        name = input("Enter the title of book you want to return: ")
        date = input("Enter the date on which the book is being returned: ")

        for book in selected_member.borrowed_books:

            if book.name.lower == name:
                book.return_date = date
                book.available = True

                selected_member.borrowed_books.remove(book)

                print(f"The book '{book.name}' has been returned successfully")

                return

        print("This book was not borrowed by this member")


    @classmethod
    def view_book(cls):
        name = input("Enter the title of the book you want to view: ")

        for book in cls.all_books:

            if name == book.name.lower:

                book.show_details()

                if book.available:
                    print("The book is available for borrowing")

                else:
                    print(f"The book is currently borrowed and will be returned on {book.return_date}")

                return

        print("Book not found")


    @classmethod
    def show_all_books_available(cls):

        if not cls.all_books:
            print("No books found!")

        else:
            for book in cls.all_books:

                if book.available:
                    book.show_details()



class Member:
    all_members = []

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

        Member.all_members.append(self)


    def show_details(self):

        print("\nMember details:")
        print(f"Name: {self.name}")
        print(f"Member ID: {self.member_id}")

        if self.borrowed_books:

            print("Borrowed books:")

            for book in self.borrowed_books:
                print(f"- {book.name}")

        else:
            print("No books borrowed")



# Creating members

member1 = Member("Sam", 1234)
member2 = Member("Max", 5678)
member3 = Member("Sophie", 9012)
member4 = Member("Silva", 3456)
member5 = Member("Adria", 7890)



# Creating books

book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("Atomic Habits", "James Clear")
book3 = Book("The Alchemist", "Paulo Coelho")
book4 = Book("Rich Dad Poor Dad", "Robert Kiyosaki")
book5 = Book("The Psychology of Money", "Morgan Housel")
book6 = Book("Ikigai", "Hector Garcia and Francesc Miralles")
book7 = Book("Sherlock Holmes", "Arthur Conan Doyle")
book8 = Book("Pride and Prejudice", "Jane Austen")
book9 = Book("The Hobbit", "J.R.R. Tolkien")
book10 = Book("1984", "George Orwell")
book11 = Book("Wings of Fire", "A.P.J Abdul Kalam")
book12 = Book("Clean Code", "Robert C. Martin")



def menu():

    while True:

        print("\n====== Library Management System ======")
        print("1. Borrow Book 📚")
        print("2. Return Book 📚")
        print("3. View Book 📖")
        print("4. Show Available Books 📚")
        print("5. Show Member Details 👤")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")


        if choice == "1":
            Book.borrow_book()


        elif choice == "2":
            Book.return_book()


        elif choice == "3":
            Book.view_book()


        elif choice == "4":
            Book.show_all_books_available()


        elif choice == "5":

            member_id = int(input("Enter member ID: "))

            for member in Member.all_members:

                if member.member_id == member_id:
                    member.show_details()
                    break

            else:
                print("Member not found")


        elif choice == "6":

            print("Exiting Library Management System. Goodbye!")

            break


        else:
            print("Invalid choice, try again!")



if __name__ == "__main__":
    menu()