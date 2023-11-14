print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the roller coaster.")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("It will be $5 to ride the roller coaster.")
  elif age <= 18:
    bill = 7
    print("It will be $7 to ride the roller coaster.")
  elif age >= 45 and age <= 55:
    bill =  0
    print("Your ticket is on the house!")
  else:
    bill = 12
    print("It will be $12 to ride the roller coaster.")
  wants_photo = input("Do you want to photo taken? Type Y or N.")
  if wants_photo == "Y":
    bill += 3
  print(f"Your total bill is going to be ${bill}.")
else:
  print("Sorry, you aren't tall enough to ride the roller coaster come back next year.")