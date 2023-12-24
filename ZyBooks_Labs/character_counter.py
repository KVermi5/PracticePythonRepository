user_character = input('Type the character you wish to count:\n')
user_phrase = input('Type the phrase you wish to count the character in:\n')

if user_character in user_phrase:
    character_count = user_phrase.count(user_character)
    if character_count > 1:
        print(f'{character_count} {user_character}\'s')
    elif character_count == 1:
        print(f'{character_count} {user_character}')
else:
    print(f'0 {user_character}\'s')