# On a piano, a key has a frequency, say f0.
# Each higher key (black or white) has a frequency of f0 * rn, where n is the distance (number of keys) from that key,
# and r is 2(1/12). Given an initial key frequency, output that frequency and the next 3 higher key frequencies


import math

f0 = float(input('Enter current piano key frequency:\n'))

r = math.pow(2, (1 / 12))

f1 = f0 * (math.pow(r, 1))
f2 = f0 * (math.pow(r, 2))
f3 = f0 * (math.pow(r, 3))

print(f'{f0:.2f} Hz\n{f1:.2f} Hz\n{f2:.2f} Hz\n{f3:.2f} Hz')
