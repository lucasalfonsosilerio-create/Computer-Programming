# Silerio, Lucas
# Computer Programming, Period 4
# Assignment: Homework 2B
# 18 September 2026

alien_color = ["green", "yellow", "red"]

if alien_color[2] == "green":
    print("Player has gotten 5 points!")
elif alien_color[2] == "yellow":
    print("Player has gotten 10 points!")
elif alien_color[2] == "red":
    print("Player has gotten 15 points!")

age = 65
stage_of_life_list = [2, 4, 13, 20, 65]

if age < stage_of_life_list[0]:
    print("This person is a baby.")
elif stage_of_life_list[1] > age > stage_of_life_list[0]:
    print("This person is a toddler.")
elif stage_of_life_list[2] > age >= stage_of_life_list[1]:
    print("This person is a kid.")
elif stage_of_life_list[3] > age >= stage_of_life_list[2]:
    print("This person is a teenager.")
elif stage_of_life_list[4] > age >= stage_of_life_list[3]:
    print("This person is an adult.")
elif age >= stage_of_life_list[4]:
    print("This person is an elder.")