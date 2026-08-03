class Student:
    all_students = []

    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def update_student_marks(self, new_marks):
        self.marks = new_marks

    def show_details(self):
        print("\nStudent details:")
        print(f"Name: {self.name}")
        print(f"Roll_number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    @classmethod
    def find_student_by_roll_number(cls, roll_number):
        for student in cls.all_students:
            if student.roll_number == roll_number:
                return student
        return None

    @classmethod
    def add_student(cls):
        name = input("Enter student's name: ")
        roll_number = input("Enter student's roll number: ")
        marks = int(input("Enter student's marks: "))

        student = cls(name, roll_number, marks)
        cls.all_students.append(student)

        print(f"Student: {name} added successfully!")

    @classmethod
    def update_marks(cls):
        roll_number = input("Enter student's roll number: ")

        student = cls.find_student_by_roll_number(roll_number)

        if student:
            new_marks = int(input("Enter student's updated marks: "))
            student.update_student_marks(new_marks)

            print(f"Marks for {student.name} updated successfully!")

        else:
            print("Student not found")

    @classmethod
    def show_all_students(cls):
        if not cls.all_students:
            print("No students found")
            return

        for student in cls.all_students:
            student.show_details()


def menu():
    while True:
        print("\n======== Student Management System ========")
        print("1. Add student")
        print("2. Update marks")
        print("3. Show all students")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            Student.add_student()

        elif choice == '2':
            Student.update_marks()

        elif choice == '3':
            Student.show_all_students()

        elif choice == '4':
            print("Exiting the student management system, Goodbye!")
            break

        else:
            print("Invalid choice, Try again!")


if __name__ == '__main__':
    menu()