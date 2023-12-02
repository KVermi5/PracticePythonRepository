user_input = input('Enter phone number:\n')
lower_input = user_input.lower()
phone_number = ''

for character in lower_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif 'a' <= character <= 'c':
        phone_number += '2'
    elif 'd' <= character <= 'f':
        phone_number += '3'
    elif 'g' <= character <= 'i':
        phone_number += '4'
    elif 'j' <= character <= 'l':
        phone_number += '5'
    elif 'm' <= character <= 'o':
        phone_number += '6'
    elif 'p' <= character <= 's':
        phone_number += '7'
    elif 't' <= character <= 'v':
        phone_number += '8'
    elif 'w' <= character <= 'z':
        phone_number += '9'
    elif character == '+':
        phone_number += '0'
    else:
        phone_number += '?'

print(f'Numbers only: {phone_number}')