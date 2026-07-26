questions = ["What is the capital of India?","How many continents are there?","Which is the largest ocean on Earth?","What is the chemical symbol for oxygen?","Which planet is known as the Red Planet?"]
options = [["A) Mumbai","B) New Delhi",
"C) Kolkata","D) Bengaluru"],["A) 5","B) 6","C) 7","D) 8"],["A) Atlantic Ocean","B) Indian Ocean","C) Arctic Ocean","D) Pacific Ocean"],["A) Ox","B) O","C) O₂","D) C"],["A) Venus","B) Jupiter","C) Mars","D) Mercury"]]
print(questions [0])
for option in options[0]:
    print(option)
Answer1 = input("Answer: ")
if Answer1 == 'B':
    print("Correct!")
else:
    print("Wrong!")
print(questions [1])
for option in options[1]:
    print(option)
Answer2 = input("Answer: ")
if Answer2 == 'C':
    print("Correct!")
else:
    print("Wrong!")
print(questions [2])
for option in options[2]:
    print(option)
Answer3 = input("Answer: ")
if Answer3 == 'D':
    print("Correct!")
else:
    print("Wrong!")
print(questions [3])
for option in options[3]:
    print(option)
Answer4 = input("Answer: ")
if Answer4 == 'C':
    print("Correct!")
else:
    print("Wrong!")
print(questions [4])
for option in options[4]:
    print(option)
Answer5 = input("Answer: ")
if Answer5 == 'C':
    print("Correct!")
else:
    print("Wrong!")
if Answer1 == 'B' and Answer2 == 'C' and Answer3 == 'D' and Answer4 == 'C' and Answer5 == 'C':
    print("Congratulations! You have a perfect score")