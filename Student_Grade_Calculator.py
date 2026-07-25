subject1 = float(input("Subject 1 marks: "))
subject2= float(input("Subject 2 marks: "))
subject3 = float(input("Subject 3 marks: "))
subject4 = float(input("Subject 4 marks: "))
subject5 = float(input("Subject 5 marks: "))
Total_marks = subject1+ subject2+subject3+subject4+subject5
print("Total_Marks:",Total_marks)
Average = round(Total_marks/5,2)
print("Average:", Average)
if subject1<30 or subject2<30 or subject3<30 or subject4<30 or subject5<30:
    print("Reault = Fail:","You scored less than 30 in a subject")
elif Average >= 90:
    print("A:","Excellent")
elif Average >= 80:
    print("B:","Good")
elif Average >= 70:
    print("C:","Satisfactory")
elif Average >= 60:
    print("D:","Can do better")
else:
    print("F:","Improvement needed")