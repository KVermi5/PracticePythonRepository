print('Input first equation, ax + by = c')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

print('Input second equation, dx + ey = f')
d = int(input('d: '))
e = int(input('e: '))
f = int(input('f: '))

check = False
for x in range(-10, 11):
    for y in range(-10, 11):
        if ((a * x) + (b * y) == c) and ((d * x) + (e * y) == f):
            check = True
            print(f'x = {x} , y = {y}')
            break
if not check:
    print('There is no solution')