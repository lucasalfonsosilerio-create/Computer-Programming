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

usernames = ["Emilia", "admin", "Jordan", "Julien", "Miguel"]

if not usernames: 
    print("Username list is empty")
else:
    for z in usernames:
        if z == "admin":
            print(f"Hello, {z.title()}, would you like a status report?")
        elif z != "admin":
            print(f"Hello {z}, welcome back.")

current_Users = ["Emi", "Sinclair", "Luna", "Grant", "Jackson"]
new_Users = ["emi", "luna", "tristan", "joaquin", "luke"]
current_Users_lowercase = [current_Users[0].lower(), current_Users[1].lower(), current_Users[2].lower(), current_Users[3].lower(), current_Users[4].lower()]

for i in new_Users:
    if i in current_Users_lowercase:
        print("This username is not avaliable, please choose a new one.")
    else:
        print("This username is avaliable.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for m in numbers:
    if m == 1:
        print(f"{m}st")
    elif m == 2:
        print(f"{m}nd")
    elif m == 3:
        print(f"{m}rd")
    else:
        print(f"{m}th")