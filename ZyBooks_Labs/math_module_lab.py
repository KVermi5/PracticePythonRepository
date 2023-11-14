# given three floating-point numbers x, y, and z, output x to the power of z, x to the power(y to
# power of z), the absolute value of (x minus y), and the square root of (x to the power of z).

import math

x = float(input('Enter x here:\n'))
y = float(input('Enter y here:\n'))
z = float(input('Enter z here:\n'))

value1 = math.pow(x, z)
value2 = math.pow(x, (math.pow(y, z)))
value3 = math.fabs(x - y)
value4 = math.sqrt(math.pow(x, z))

print(f'{value1:.2f} {value2:.2f} {value3:.2f} {value4:.2f}')