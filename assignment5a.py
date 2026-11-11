# Silerio, Lucas
# Computer Programming, period 4
# Assignment: Homework 5a
# 11 November 2026

#problem 1
restaurant_seating = int(input("How many people are being seated in your group?"))

if restaurant_seating > 8:
    print("Wait for a table")
else:
    print("There's a table ready for you")

#problem 2
multiple_of_ten = int(input("Input a number"))

if multiple_of_ten % 10 == 0:
    print("multiple of ten")
else:
    print("not a multiple of ten")

#problem 3
while True:
    pizza_topping = input("input a pizza topping ")

    if pizza_topping.strip().lower() == "quit":
        break
    else:
        print(f"adding {pizza_topping} to pizza")

#problem 4
age = 0

while age != "quit":
    age = input("how old are you").strip()

    if age == "quit":
        break
    elif int(age) < 3:
        print("free ticket")
    elif 3 <= int(age) <= 12:
        print("ticket costs $10")
    elif int(age) > 12:
        print("ticket costs $15")

#problem 5 & 6
finished_sandwich = []
sandwich_orders = []

while True:
    add_sandwich = input("sandwich here ").strip().lower()

    if add_sandwich == "quit":
        break
    else:
        sandwich_orders.append(add_sandwich)

if sandwich_orders.count("pastrami") >= 3:
    print("we're out of pastrami")
    while sandwich_orders.count("pastrami") > 0:
        sandwich_orders.remove("pastrami")

for i in sandwich_orders:
    print(f"I made your {i}")
    finished_sandwich.append(i)

print(finished_sandwich)

#problem 7
dream_vacation = []

while True:
    vacation_dest = input("Where would you like to go on a dream vacation?").strip().lower()

    if vacation_dest == "quit":
        break
    else:
        dream_vacation.append(vacation_dest)

for x in dream_vacation:
    print(f"One user wants to go to {x}")