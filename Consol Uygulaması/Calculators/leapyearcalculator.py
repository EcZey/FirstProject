def leapYearCalculator():
    year_ = int(input("Enter a year: "))
    if year_ % 4 == 0:
        if year_ % 100 == 0:
            if year_ % 400 ==0:
                print("Leap year")
            else:
                print("Not leap")
        else:
            print("Leap year")
    else:
        print("this year is not a leap year")

#leapYearCalculator()