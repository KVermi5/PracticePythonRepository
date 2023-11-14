names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
import random

num_names = len(names)

random_name = random.randint(0, num_names - 1)
print(names[random_name], "is going to buy the meal today!")

