stop = False

print('Welcome to my Mad Lib generator! Please enter a word and a number here:\n')

while stop == False:
    user_input = input().split()
    word = user_input[0]
    integer = user_input[1]

    if word != 'quit':
        print(f'Eating {integer} {word} a day keeps the doctor away.')
        print('Please enter another word and a number or type \"quit\" to exit:\n')
    else:
        stop = True