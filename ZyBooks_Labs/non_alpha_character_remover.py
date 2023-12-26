user_input = input()
string=''

for char in user_input:
    if char.isalpha():
        string += char

print(string)
