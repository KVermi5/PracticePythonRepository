# 2 = abc
# 3 = def
# 4 = ghi
# 5 = jkl
# 6 = mno
# 7 = pqrs
# 8 = tuv
# 9 = wxyz
# 0 = +
user_input = input('Enter phone number:\n')
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
        phone_number += '2'
    elif ('d' <= character <= 'f') or ('D' <= character <= 'F'):
        phone_number += '3'
    elif ('g' <= character <= 'i') or ('G' <= character <= 'I'):
        phone_number += '4'
    elif ('j' <= character <= 'l') or ('J' <= character <= 'L'):
        phone_number += '5'
    elif ('m' <= character <= 'o') or ('M' <= character <= 'O'):
        phone_number += '6'
    elif ('p' <= character <= 's') or ('P' <= character <= 'S'):
        phone_number += '7'
    elif ('t' <= character <= 'v') or ('T' <= character <= 'V'):
        phone_number += '8'
    elif ('w' <= character <= 'z') or ('W' <= character <= 'Z'):
        phone_number += '9'
    elif character == '+':
        phone_number += '0'
    else:
        phone_number += '?'

print(f'Numbers only: {phone_number}')