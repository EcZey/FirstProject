def bmiCalculator():
    weight=float(input("please enter your weight:"))
    height=float(input("please enter your height: "))
    bmi= round(weight/height**2)
    if bmi > 25:
        print("you are overweight")
    elif bmi < 18.5:
        print("you are underweight")
    else:
        print(bmi, "you are normal weight")