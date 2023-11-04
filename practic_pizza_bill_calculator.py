print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza would you like to order? Enter 'S' for small, 'M' for medium, or 'L' for large.") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Enter Y or N.")
extra_cheese = input("Do you want extra cheese? Enter Y or N.")
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
if size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
if size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill+= 3
if extra_cheese == "Y":
  bill += 1
print(f"Your final bill is: ${bill}.")