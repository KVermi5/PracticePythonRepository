# write a program that takes a date as input and
# outputs the dates season in the northern hemisphere
# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

input_month = str(input('Enter the month here:'))
input_day = int(input('Enter the day here:'))

lower_month = input_month.lower()

months_31_days = ('january', 'march', 'may', 'july', 'august', 'october', 'december')
spring = ('march', 'april', 'may', 'june')
summer = ('june', 'july', 'august', 'september')
autumn = ('september', 'october', 'november', 'december')
winter = ('december', 'january', 'february', 'march')

if (input_day >= 32) or (input_day <= 0):
    print('Invalid')
elif (input_day >30) and (lower_month not in months_31_days):
    print('Invalid')
elif lower_month in spring:
    if lower_month == 'march':
        season = 'Spring' if (input_day >= 20) else 'Winter'
        print(season)
    elif lower_month == 'june':
        season = 'Spring' if (input_day <= 20) else 'Summer'
        print(season)
    else:
        print('Spring')
elif lower_month in summer:
    if lower_month == 'september':
        season = 'Summer' if (input_day <= 21) else 'Autumn'
        print(season)
    else:
        print('Summer')
elif lower_month in autumn:
    if lower_month == 'december':
        season = 'Autumn' if (input_day <= 20) else 'Winter'
        print(season)
    else:
        print('Autumn')
elif lower_month in winter:
    print('Winter')
else:
    print('Invalid')