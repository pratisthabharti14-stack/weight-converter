height = float(input("Enter your height: "))
unit1 = input("(M)etre or (F)eet: ").upper()

weight = float(input("Enter your weight: "))
unit2 = input("(K)g or (L)bs: ").upper()

if unit1 == 'M' and unit2 == 'K':
    converted = weight / (height * height)
    print("BMI:", str(converted))

elif unit1 == 'F' and unit2 == 'L':
    converted = weight * 703 / (height * height)
    print("BMI:", str(converted))

elif unit1 == 'M' and unit2 == 'L':
    converted = weight * 0.453592 / (height * height)
    print("BMI:", str(converted))

elif unit1 == 'F' and unit2 == 'K':
    converted = weight / (height * 0.3048 * height * 0.3048)
    print("BMI:", str(converted))

else:
    print("Invalid Unit")

if converted < 18.5:
    print("Underweight")
elif converted < 25:
    print("Healthy weight")
elif converted < 30:
    print("Overweight")
else:
    print("Obesity")