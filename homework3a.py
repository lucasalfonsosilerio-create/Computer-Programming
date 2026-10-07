alien_color = ["green", "yellow", "red", "blue"]

for i in alien_color:
    if i == "green":
        print("player earned 5 points")
    elif i == "yellow":
        print("player earned 10 points")
    elif i == "red":
        print("player earned 15 points")
    else:
        print("player earned no points")

age = [1, 3.9, 10, 13, 19, 20, 21, 65]

for x in age:
    if x >= 65:
        print("person is an elder")
    elif 65 > x >= 20:
        print("person is an adult")
    elif 20 > x >= 13:
        print("person is a teenager")
    elif 13 > x >= 4:
        print("person is a kid")
    elif 4 > x >= 2:
        print("person is a toddler")
    elif x < 2:
        print("person is a baby")

usernames = ["emi", "luna", "admin", "trump", "grant"]

for y in usernames:
    if y == "admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {y.title()}, welcome back.")

current_users = ["fartmaster", "emi", "luna", "grantinator", "rizzler"]
new_users = ["Fartmaster", "EmI", "123savesomeforme", "skibidiler", "jackson"]
new_users_lower = []
for a in range(0, len(new_users)):
    new_users_lower.append(new_users[a].lower())

for z in current_users:
    if z.lower() in new_users_lower:
        print("Username is already taken, please choose a new username.")
    else:
        print("Username is not taken.")

ordinal_numbers = [1,2,3,4,5,6,7,8,9]

for b in ordinal_numbers:
    if b == 1:
        print("1st")
    elif b == 2:
        print("2nd")
    elif b == 3:
        print("3rd")
    else:
        print(f"{b}th")