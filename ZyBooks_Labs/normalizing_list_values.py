list_length = int(input('Enter the number of data values to be normalized:'))
listval = []
n = 0
y = 0
i = 0
for n in range(list_length):
    userval = float(input('Enter data value:'))
    listval.append(userval)
valmax = max(listval)

for userval in listval:
    userval = userval / valmax
    if 1 >= userval >= 0:
        print(f'{userval:.2f}')
    else:
        continue