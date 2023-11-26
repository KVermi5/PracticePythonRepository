# every 4 years a leap year takes place consisting of 366 days instead of 365
# This extra day is February 29th.
# to be a leap year:
# must be divisible by 4
# if a century year, it must be evenly divisible by 400
# test inputs 1600, 1712, 2016
# use statement print(f'{input_year} - leap year) or print(f'{input_year} - not  a leap year)

is_leap_year = False

print('Welcome to the leap year calculator!')
input_year = int(input('Enter the year you want to check here:'))

if (input_year % 100) == 0:
    if (input_year % 400) == 0:
        is_leap_year = True
    else:
        print(f'{input_year} - not a leap year')
elif (input_year % 4) == 0:
    is_leap_year = True
else:
    print(f'{input_year} - not a leap year')

if is_leap_year == True:
    print(f'{input_year} - leap year')