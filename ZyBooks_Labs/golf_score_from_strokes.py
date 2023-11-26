par = int(input('Enter the par here:'))
num_strokes = int(input('Enter the number of strokes here:'))

if (par == 3) or (par == 4) or(par == 5):
    if num_strokes == (par - 2):
        print('Eagle')
    elif num_strokes == (par - 1):
        print('Birdie')
    elif num_strokes == par:
        print('Par')
    elif num_strokes == (par + 1):
        print('Bogey')
else:
    print('Error')