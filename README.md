# weight-converter
# Weight Converter Utility

A simple and interactive command-line Python application that converts weight measurements seamlessly between Kilograms (Kg) and Pounds (Lbs).

## 🚀 Features
- **Accurate Conversion Math**: Converts Kg to Lbs (multiplies by 2.20462) and Lbs to Kg (divides by 2.20462).
- **Case-Insensitive Inputs**: Accepts both lowercase and uppercase unit selections (`k`, `K`, `l`, `L`).
- **Cloud-Ready**: Fully configured to open and run instantly inside GitHub Codespaces.

## 🛠️ How to Run

### Option 1: In the Cloud (GitHub Codespaces)
1. Click the green **Code** button at the top of this repository.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Once the terminal loads at the bottom, type:
   ```bash
   python weight.py
   ```

### Option 2: Locally on Your Computer
1. Download this repository as a ZIP file and extract it.
2. Open your terminal or command prompt inside the project folder.
3. Run the script using:
   ```bash
   python weight.py

## Basic Calculator 🧮

A simple calculator program written in Python.

### Features
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Takes user input for two numbers
- Allows the user to choose an operation
- Runs continuously until the user types `exit`
- Prevents division by zero

### Concepts Practiced
- Variables
- `input()`
- `float()`
- `if`, `elif`, and `else`
- Arithmetic operators
- `print()`
- 'while loop'
- `break`
- Nested `if` statements

### Example

```text
First number: 10
Second number: 5
Enter + or - or * or /: *
50.0
```


# Temperature Converter Utility

A simple and interactive command-line Python application that converts temperature measurements seamlessly between Fahrenheit (F) and Celsius (C).

🚀 Features

* **Accurate Conversion Math:** Converts Fahrenheit to Celsius (subtracts 32, then divides by 1.8) and Celsius to Fahrenheit (multiplies by 1.8, then adds 32).
* **Case-Insensitive Inputs:** Accepts both lowercase and uppercase unit selections (`f`, `F`, `c`, `C`).
* **Cloud-Ready:** Fully configured to open and run instantly inside GitHub Codespaces.

🧠 Topics Learned

* **Data Type Casting:** Learned how to convert raw user string inputs into numbers using `float()`.
* **String Methods:** Mastered text normalization techniques using `.upper()` for easy logic validation.
* **Conditional Control Flow:** Implemented multi-way decision-making blocks using `if`, `elif`, and `else`.
* **Version Control Basics:** Practiced identifying syntax bugs, resolving runtime errors, and committing code directly to GitHub.

🛠️ How to Run

Option 1: In the Cloud (GitHub Codespaces)
1. Click the green **Code** button at the top right of this repository.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Once the environment loads, run the app in the integrated terminal:
   ```bash
   python "temperature converter.py"
   ```

Option 2: On Your Local Machine
1. Ensure you have **Python 3** installed on your computer.
2. Clone this repository or download the source file to your device.
3. Open your terminal or command prompt, navigate to the project directory, and run:
   ```bash
   python "temperature converter.py"


   ```
# My Family - Python OOP

A simple Python project created while learning Object-Oriented Programming (OOP).

## What I Learned

- Creating a class
- Using the `__init__()` constructor
- Creating objects
- Using instance attributes
- Creating and calling methods

## Description

The `My_Family` class stores information about family members, including:

- Name
- Relation
- Age
- Occupation

The program creates multiple family member objects and displays their information.

## Concepts Used

- Python
- Classes
- Objects
- Constructors
- Instance attributes
- Methods
  ```
# Customer Count

A simple Python program that demonstrates the basics of **Object-Oriented Programming (OOP)** using a `Customer` class.

## Features

- Creates customer objects using a class.
- Stores customer information:
  - Customer name
  - Order
  - Token number
- Displays customer details using a method.
- Automatically counts the total number of customers using a class variable.

## Concepts Practiced

- Classes and Objects
- `__init__()` Constructor
- Instance Attributes
- Instance Methods
- Class Variables
- `self`
- Formatted Strings (f-strings)

## Example

The program creates three customers:

- Max → Bulgogi → Token 14
- Bruce → Bibimbap → Token 15
- Mary → Kalguksu → Token 16

### Output

```text
Customer_Name: Max, Order: Bulgogi, Token_Number: 14
Customer_Name: Bruce, Order: Bibimbap, Token_Number: 15
Customer_Name: Mary, Order: Kalguksu, Token_Number: 16
Total Customers: 3
  ```
# Bank Account

A simple Python program that demonstrates Object-Oriented Programming (OOP) concepts by creating a basic `BankAccount` class.

## Features

- Creates a bank account with an owner and initial balance.
- Allows money to be deposited into the account.
- Validates deposit amounts to ensure they are positive.
- Logs transactions using a private method.
- Uses name mangling for private members.
- Validates interest rates using a static method.
- Defines a minimum balance as a class variable.

## Concepts Practiced

- Classes and Objects
- `__init__()` Constructor
- Instance Attributes
- Class Variables
- Instance Methods
- Private Attributes
- Name Mangling
- Private Methods
- `@staticmethod`
- Encapsulation
- Data Validation
- f-strings

## Example

The program creates a bank account for Alice with an initial balance of `$550`.

It then:

1. Deposits `$200`.
2. Logs a transaction.
3. Checks whether an interest rate of `4%` is valid.

### Example Output

```text
Logging deposit of $200. New balance: 750
Alice's new balance: $750
Logging withdraw of $200. New balance: 750
True
 ```
# BMI Calculator

This is a simple **BMI (Body Mass Index) Calculator** built using Python. The program allows users to enter their height and weight using different units and calculates their BMI.

## Features

- Accepts height in:
  - Metres (M)
  - Feet (F)
- Accepts weight in:
  - Kilograms (K)
  - Pounds (L)
- Supports different combinations of height and weight units.
- Automatically converts units while calculating BMI.
- Displays the calculated BMI.
- Categorizes BMI as:
  - Underweight
  - Healthy weight
  - Overweight
  - Obesity
- Uses conditional statements and user input handling.

## How It Works

The user enters:

1. Their height
2. The unit of their height (`M` for Metres or `F` for Feet)
3. Their weight
4. The unit of their weight (`K` for Kilograms or `L` for Pounds)

The program then calculates the BMI based on the selected units.

### BMI Categories

| BMI Range | Category |
|-----------|----------|
| Below 18.5 | Underweight |
| 18.5 – 24.9 | Healthy weight |
| 25 – 29.9 | Overweight |
| 30 and above | Obesity |

## Concepts Used

This project helped me practice:

- `input()` function
- `float()` type conversion
- `.upper()` string method
- `if`, `elif`, and `else` statements
- Arithmetic operations
- Variables
- Unit conversion
- Conditional logic

## Example

```text
Enter your height: 1.75
(M)etre or (F)eet: M
Enter your weight: 65
(K)g or (L)bs: K

BMI: 21.22448979591837
Healthy weight
   ```
# Student Grade Calculator

This is a simple **Student Grade Calculator** built using Python. The program takes marks for five subjects, calculates the total marks and average, and assigns a grade based on the student's average.

The program also checks whether the student has scored below the minimum passing mark in any subject.

## Features

- Accepts marks for 5 subjects.
- Calculates the total marks.
- Calculates the average and rounds it to 2 decimal places.
- Checks whether the student has scored less than 30 marks in any subject.
- Assigns a grade based on the average.
- Displays feedback for each grade.
- Automatically marks the student as **Fail** if any subject score is below 30.

## Grading System

| Average | Grade | Feedback |
|---------|-------|----------|
| 90 and above | A | Excellent |
| 80 – 89 | B | Good |
| 70 – 79 | C | Satisfactory |
| 60 – 69 | D | Can do better |
| Below 60 | F | Improvement needed |

### Passing Requirement

A student must score at least **30 marks in every subject** to pass.

If the student scores below 30 in even one subject, the final result will be:

```text
Fail: You scored less than 30 in a subject
  ```
# Python Quiz Game

A simple multiple-choice quiz game built using Python. The program asks the user a series of general knowledge questions, displays multiple-choice options, and checks whether the user's answers are correct.

## Features

- Multiple-choice questions
- Displays questions and answer options
- Takes answers from the user using `input()`
- Checks answers and displays whether they are correct or wrong
- Uses lists to store questions, options, and answers
- Uses `for` loops to display answer options

## Concepts Used

- Python Lists
- Nested Lists
- `input()` function
- `print()` function
- `if-else` statements
- `for` loops
- Indexing
- User input and comparison

## How It Works

1. The program stores questions in a list.
2. The options for each question are stored in a nested list.
3. The program displays a question and its corresponding options.
4. The user enters their answer.
5. The program compares the user's answer with the correct answer.
6. The program displays `Correct!` or `Wrong!`.

## Example

```text
What is the capital of India?

A) Mumbai
B) New Delhi
C) Kolkata
D) Bengaluru

Answer: B

Correct!
 ```
# Monthly Expense Tracker

A simple Python program that helps users calculate their monthly expenses, track their total spending, compare expenses with a monthly budget, and calculate their remaining savings.

## Features

- Displays different expense categories:
  - Accommodation
  - Food
  - Travel
  - Extra
- Allows the user to enter expenses manually.
- Calculates accommodation expenses using:
  - Monthly rent
  - Water bill
  - Electricity bill
- Calculates the total monthly expenses.
- Displays the updated total after every expense entry.
- Allows the user to enter their monthly budget.
- Calculates the amount left from the budget as savings.
- Checks whether the total expenses exceed the monthly budget.
- Displays how much the expenses exceed the budget when applicable.
- Uses a `for` loop to allow multiple expense entries.

## Concepts Used

This project was created to practice:

- `print()` statements
- `input()` function
- Variables
- Lists
- `for` loops
- `if`, `elif`, and `else` statements
- `float()` for numerical input
- Arithmetic operations
- Increment operators (`+=`)
- Comparison operators
- Basic budget calculations

## How It Works

The program first displays four expense categories. The user selects an expense category and enters the required amount.

For accommodation, the program calculates:

```text
Monthly Rent + Water Bill + Electricity Bill
  ```
# Expense Tracker

A simple Python expense tracker that uses file handling to save and view expenses.

## Features

- Add new expenses
- Save expenses to a text file
- View all saved expenses
- Uses append mode to add new expenses without deleting previous ones
- Uses read mode to read saved expenses
- Uses `with open()` for file handling
- Menu-driven interface

## File Handling Concepts Used

- `open()` – Opens or creates a file
- `"a"` – Opens a file in append mode
- `"r"` – Opens a file in read mode
- `write()` – Writes expenses to the file
- `read()` – Reads the contents of the file
- `with open()` – Automatically closes the file after use
- `\n` – Adds a new line after each expense

## How It Works

The program displays three options:

1. Add Expense
2. View Expenses
3. Exit

When **Add Expense** is selected, the user enters an expense. The expense is saved in `expenses.txt` using append mode.

When **View Expenses** is selected, the program reads `expenses.txt` and displays all saved expenses.

## Example

```text
1. Add Expense
2. View Expenses
3. Exit

Enter your choice: 1
Enter your Expense: ₹500

Expense added successfully
  ```
# Library Book Management

A simple Python project that demonstrates Object-Oriented Programming (OOP) and File Handling by storing and managing borrowed book information.

## Features

- Creates a `Book` class with:
  - Book name
  - Borrow date
  - Return date
  - Lender name
- Creates multiple `Book` objects.
- Displays book information using `print()`.
- Saves book information to a text file.
- Uses write mode (`"w"`) to store the first book.
- Uses append mode (`"a"`) to add another book.
- Uses read mode (`"r"`) to read and display the saved information.

## Concepts Used

- Classes and Objects
- `__init__()` constructor
- Instance attributes
- Object creation
- File handling
- `open()`
- Write mode (`"w"`)
- Append mode (`"a"`)
- Read mode (`"r"`)
- `file.write()`
- `file.read()`
- `with open()`
- Newline character (`\n`)

## How It Works

1. A `Book` class is created with four attributes.
2. Two book objects are created with their respective details.
3. The first book is written to `borrowed_books.txt`.
4. The second book is appended to the same file.
5. The program reads the file and displays all the stored information.

  ```

🎓 Student Management System

A Python-based Student Management System that helps manage student information, marks, and academic records. This project was created using Object-Oriented Programming (OOP) concepts in Python.

🚀 Features

- 👤 Add student records
- 📝 Store student name, roll number, and marks
- 📊 Update student marks
- 🔍 View student details
- 📋 Manage multiple students
- 🖥️ Menu-driven interface

🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

🧠 OOP Concepts Used

This project demonstrates:

- Classes and Objects
- Constructors ("__init__")
- Instance variables
- Class variables
- Methods
- Object management using lists

📂 Project Structure

Student-Management-System/
│
├── student_management.py
└── README.md

⚙️ How to Run

1. Clone this repository:

git clone https://github.com/your-username/Student-Management-System.git

2. Navigate to the project folder:

cd Student-Management-System

3. Run the Python file:

python student_management.py

🎮 Usage

The program allows users to manage student records through a simple menu system.

Example operations:

====== Student Management System ======

1. Add Student
2. View Student Details
3. Update Marks
4. Show All Students
5. Exit

Users can:

- Enter student details
- Store academic information
- Update marks when required
- Display student records

📌 Example Student Record

Student Details:

Name: Alex
Roll Number: 101
Marks: 92

🔮 Future Improvements

- 💾 Add file handling to save student data permanently
- 🔍 Add search functionality by roll number
- 📊 Calculate grades automatically
- 📈 Generate student performance reports
- 🖥️ Build a GUI using Tkinter
- 🌐 Convert into a web-based application

👩‍💻 Author

Pratistha Bharti

A Python project developed while learning Object-Oriented Programming and building real-world applications.
   

   ```
# 📚 Library Management System

A Python-based **Library Management System** that allows users to manage books, members, borrowing, and returning operations. This project was built using **Object-Oriented Programming (OOP)** concepts in Python.

## 🚀 Features

- 📖 Add and manage books
- 👤 Manage library members
- 🔍 Search and view book details
- 📚 Borrow books using member ID
- 🔄 Return borrowed books
- ✅ Track book availability
- 📝 Track borrowed books for each member
- 📋 View available books
- 🖥️ Menu-driven interface

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

## 🧠 OOP Concepts Used

This project demonstrates:

- **Classes and Objects**
- **Constructors (`__init__`)**
- **Class Variables**
- **Class Methods**
- **Object Attributes**
- **Encapsulation**
- **Working with Lists of Objects**

  ```
GitHub Profile Scraper

A simple Python project that uses "requests" and "BeautifulSoup" to scrape a GitHub user's profile page and extract their profile image URL.

Features

- Takes a GitHub username as input
- Fetches the user's profile page
- Parses the HTML with BeautifulSoup
- Extracts and prints the profile image URL

Requirements

pip install requests beautifulsoup4

Usage

Run the Python script and enter a GitHub username when prompted.

This project was built as a practice exercise for learning HTTP requests and web scraping with Python.
   

# Countdown Timer

A simple Python countdown timer that takes the time in seconds as input and displays the remaining time in `MM:SS` format.

## Features

- Converts seconds into minutes and seconds
- Updates every second
- Displays "Time's up!" when finished

## Requirements

- Python 3.x
- Built-in `time` module

## How to Run

Run the program and enter the desired time in seconds.

Example:

    Enter the time in seconds: 60