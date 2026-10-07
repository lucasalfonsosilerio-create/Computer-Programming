# Silerio, Lucas
# Computer Programming, Period 4
# Assignment: Homework 2
# 6 October 2026

print("backstory here")

def turn1():
    print("intriguing story here")

while True:
    direction = input("Direction: ").lower().strip()

    if directions_taken == 1:
        if direction == "right":
            print("you die")
            directions_taken = directions_taken + 1
            print(directions_taken)
            break
        elif direction == "left":
            print("intriguing story here")
            directions_taken = directions_taken + 1
            print(directions_taken)
        elif direction == "down":
            print("door closes behind you")
            directions_taken = directions_taken + 1
        elif direction == "up":
            print("meowww")
            directions_taken = directions_taken + 1
        else:
            print("i don't think you can go that way")
    elif directions_taken == 2:
        if direction == "right":
            print("you SUCK")
            break
        elif direction == "left":
            print("67")
        elif direction == "down":
            print("89")
        elif direction == "up":
            print("fuck my life")
        else:
            print("i don't think you can go that way")