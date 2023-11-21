# odd numbered U.S. interstate highways go north/south
# even numbered highways go east/west, auxiliary highways are
# numbered 100 - 999 and service the highway indicated by the two
# rightmost digits i.e. I-405 services I-5 and I-290 services I-90 given a highway
# number indicate whether it is a primary or auxiliary highway. If auxiliary
# indicate primary highway served. Indicate the direction primary highway runs.
# Test 90, 290, 0

highway_number = int(input('Enter the U.S. Interstate Highway Number here:\n'))

if (highway_number > 999) or (highway_number < 1) or (highway_number % 100 == 0):
    print(f'{highway_number} is not a valid interstate highway number.')
elif highway_number > 100:
    if (highway_number % 2) == 0:
        print(f'I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going east/west.')
    else:
        print(f'I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going north/south.')
elif (highway_number % 2) == 0:
    print(f'I-{highway_number} is primary, going east/west.')
else:
    print(f'I-{highway_number} is primary, going north/south.')