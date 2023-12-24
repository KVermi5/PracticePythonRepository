user_input = input()
full_name = user_input.split(' ')

first_name = full_name[0]
first_initial = first_name[0]

if len(full_name) >= 3:
    middle_name = full_name[1]
    middle_initial = middle_name[0]
    last_name = full_name[2]
    print(f'{last_name}, {first_initial}.{middle_initial}.')
else:
    last_name = full_name[1]
    print(f'{last_name}, {first_initial}.')