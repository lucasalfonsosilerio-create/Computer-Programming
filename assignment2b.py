# Silerio, Lucas
# Computer Programming, Period 4
# Assignment: Homework 2B
# 18 September 2026

alien_color = ["green", "yellow", "red"]

for y in alien_color:
    if y == "green":
        print("Player has gotten 5 points!")
    elif y == "yellow":
        print("Player has gotten 10 points!")
    elif y == "red":
        print("Player has gotten 15 points!")

age = [1, 3.9, 10, 13, 19, 20, 21, 65]
stage_of_life_list = [2, 4, 13, 20, 65]

for x in age:
    if x < stage_of_life_list[0]:
        print(f"At {x}, this person is a baby.")
    elif stage_of_life_list[1] > x > stage_of_life_list[0]:
        print(f"At {x}, this person is a toddler.")
    elif stage_of_life_list[2] > x >= stage_of_life_list[1]:
        print(f"At {x}, this person is a kid.")
    elif stage_of_life_list[3] > x >= stage_of_life_list[2]:
        print(f"At {x}, this person is a teenager.")
    elif stage_of_life_list[4] > x >= stage_of_life_list[3]:
        print(f"At {x}, this person is an adult.")
    elif x >= stage_of_life_list[4]:
        print(f"At {x}, this person is an elder.")

usernames = []