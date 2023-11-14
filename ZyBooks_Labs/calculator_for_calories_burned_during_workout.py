# create a program that outputs the average calorie burn for a person using input age(years),
# weight(pounds), heart rate (beats per minute), and time(minutes)

# Calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368

age = float(input('Enter your age here in years:\n'))
weight = float(input('Enter your weight here in pounds:\n'))
heart_rate = float(input('Enter your heart beats per minute here:\n'))
time = float(input('Enter the time you exercised in minutes here:\n'))

calories = ((age * 0.2757) + (weight * 0.03295) + (heart_rate * 1.0781) - 75.4991) * time / 8.368
print(f'Calories: {calories:.2f} calories')