# Silerio, Lucas
# Computer Programming, period 4
# Assignment: Homework 2A
# Sep 9, 2026

hobbies = ["video games", "playing with the dog", "coding", "sleeping", "watching youtube"]
print(hobbies, len(hobbies), hobbies[2], hobbies[0])

hello = ["hello"]*100
print(hello)

list1 = ["pumpkin", "halloween", "jack-o-lantern", "spooky"]
list2 = ["christmas", "new year", "holiday", "santa"]

list3 = list1 + list2
print(list3)

favFoods = ["french fries", "chicken nuggets", "burger", "fried rice", "ice cream"]
print(len(favFoods))
print(favFoods[-5])

favFoods.append("Lucas")
favFoods.insert(2, "17")
print(favFoods)

favFoods.remove("fried rice")
print(favFoods)

one = 1
for x in range(0, 20):
    print(one + x)

for x in range(0, 20, 2):
    print(one + x)

animals = ["tiger", "lion", "panther"]

for y in animals:
    print(f"A {y} counts as a cat.")
else:
    print("All of these animals are dangerous!")

guest_list = ["Einstein", "Aristotle", "Newton"]
for z in guest_list:
    print(f"{z} is invited to my dinner.")
print("Aristotle can't make it.")
guest_list.append("Obama")
for z in guest_list:
    print(f"{z} is invited to my dinner")
    if z == "Aristotle":
        continue