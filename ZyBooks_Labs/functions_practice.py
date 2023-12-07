size = 5
# 5 99 -44 0 12


def get_numbers(num):
    numbers = []
    user_input = input(f'Enter {num} integers:\n')

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers


def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:', end='')
    for num in numbers:
        print(num, '', end='')
    print()


def print_odd_numbers(numbers):
    # Print all odd numbers
    print('Odd numbers:', end='')
    for num in numbers:
        if num % 2 != 0:
            print(num, '', end='')
    print()


def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:', end='')
    for num in numbers:
        if num < 0:
            print(num, '', end='')
    print()


nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)