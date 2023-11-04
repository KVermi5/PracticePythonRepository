print("Welcome to Treasure Island! Your mission is to find the treasure.")
direction = input("Fantastic! Now, left or right?")
lower_direction = direction.lower()
if lower_direction == "right":
    print("Game Over.")
if lower_direction == "left":
    swim_wait = input("swim or wait?")
    lower_swim_wait = swim_wait.lower()
    if lower_swim_wait == "swim":
        print("Game Over.")
    if lower_swim_wait == "wait":
        door_color = input("Which door? Blue, Yellow, Red?")
        lower_door_color = door_color.lower()
        if lower_door_color == "blue":
            print("Game Over.")
        if lower_door_color == "red":
            print("Game Over.")
        if lower_door_color == "yellow":
            print("You Win!")
