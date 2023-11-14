
height = input("Please enter your height in meters:")

weight = input("Please enter your weight in kilograms:")

height = float(height)
bmi = float(weight) / (height ** 2)

print(int(bmi))