print("wewcome to the tip cawcuwatow. >_<")

bill = float(input("What is the total bill?\n$"))
tip_percentage = float(input("What percentage tip will you like to give?\n"))
split_among = int(input("How many people to split the bill?\n"))

total_bill_with_tip = bill + (bill * tip_percentage / 100)
each_pay = total_bill_with_tip / split_among

print(f"Each person should pay: ${round(each_pay, 2)}")