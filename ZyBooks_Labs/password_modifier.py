print('Hello, use this program to strengthen your password!')
word = input('Enter the password here:\n')
password = ''
for i in range(int(len(word))):
    if word[i] == 'i':
        character = '1'
    elif word[i] == 'a':
        character = '@'
    elif word[i] == 'm':
        character = 'M'
    elif word[i] == 'B':
        character = '8'
    elif word[i] == 's':
        character = '$'
    else:
        character = word[i]
    password = password + character
print(password + '!')