print("So you found my tip calculator?")
print("Alright, then give me some numbers to work with I don't have all day!")
bill_total = input("How much was the bill?")
people_on_bill = input("How many people are splitting the bill with you?")
tip_percentage = input("How much are you planning to tip? 10? 12? 15?")

tip_percentage = float(tip_percentage) / 100
tip_percentage = float(tip_percentage) * float(bill_total)
bill_with_tip = float(bill_total) + float(tip_percentage)
your_share = float(bill_with_tip) / float(people_on_bill)

print(f"Each person should pay ${round(your_share, 2)}")
print("Now get out of here!")