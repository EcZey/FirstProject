def tipCalculator():
    print("Welcome to the tip calculator")
    bill= float(input("please enter the bill amount: "))
    tip= int(input("What percentage would you like to give? 10, 12, 15? :"))
    people= int(input("How many people are splitting the bill? :"))
    tip= tip/100
    total_bill= (bill* tip) + bill
    result=round(total_bill/people,2)
    print(f"Each person should pay: {result}")