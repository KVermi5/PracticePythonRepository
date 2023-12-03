print('Welcome, use this calculator to convert a positive integer to a binary number in reverse.')
print()
print('For example: 6 results in a binary number 110 output in reverse as 011.')
print()

user_input = int(input('Input a positive integer here to convert:'))
x = user_input
y = 0
while x > 0:
    y = x % 2
    if (y == 0) or (y == 1):
        print(y, end='')
    x = int(x / 2)