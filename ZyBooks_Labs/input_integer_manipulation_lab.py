# using floor division write a program that reads integers user_num and div_num as input
# and outputs user_num divided by div_num three times
user_num = int(input('Enter your first number here:\n'))
div_num = int(input('Enter the number you want to divide it by here:\n'))

num1 = user_num // div_num
num2 = num1 // div_num
num3 = num2 // div_num

print(num1, num2, num3)