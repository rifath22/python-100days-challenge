print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill ? $"))
no_of_people = int(input("Please enter the number of person to split the bill"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
tip_percentage = tip/100 + 1
one_person = (total_bill/no_of_people) * tip_percentage
rounding_the_money = round(one_person, 2)

print(f"Each person should pay: ${rounding_the_money}")