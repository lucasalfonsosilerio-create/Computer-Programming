# Silerio, Lucas
# Computer Programming, period 4
# Assignment: Star Map
# Oct 28, 2027

total_mass_list = []
total_mass = 0

stars = {
    "Sun" : {"x" : 0.0, "y" : 0.0, "z" : 0.0, "luminosity" : 1.0, "mass" : 1.0},
    "Sirius" : {"x" : -1.6, "y" : 8.1, "z" : -2.5, "luminosity" : 25.4, "mass" : 2.06},
    "Vega" : {"x" : 7.2, "y" : -4.5, "z" : 25.3, "luminosity" : 40.0, "mass" : 2.14},
    "Proxima Centauri" : {"x" : 1.6, "y" : -3.8, "z" : -1.2, "luminosity" : 0.0017, "mass" : 0.12},
    "Betelgeuse" : {"x" : 88.0, "y" : -120.0, "z" : 45.0, "luminosity" : 100000.0, "mass" : 16.5}
}

print(len(stars))

print(stars["Sirius"]["mass"])
print(f"({stars["Vega"]["x"]}, {stars["Vega"]["y"]}, {stars["Vega"]["z"]})")

for i in stars.keys():
    print(f"{i}: pos: ({stars[i]["x"]}, {stars[i]["y"]}, {stars[i]["z"]}), luminosity: {stars[i]["luminosity"]}, mass: {stars[i]["mass"]}")
    total_mass_list.append(stars[i]["mass"])
    total_mass = total_mass + stars[i]["mass"]

average_mass = total_mass/len(total_mass_list)

print(total_mass, average_mass)

stars["Proxima Centauri"]["mass"] = 0.122
stars["Buzz"] = {"x" : 67.0, "y" : -6.7, "z" : 6.9, "luminosity" : 4489.0, "mass" : 21.6}
del(stars["Betelgeuse"])

total_mass_list_1 = []
total_mass_1 = 0

for i in stars.keys():
    print(f"{i}: pos: ({stars[i]["x"]}, {stars[i]["y"]}, {stars[i]["z"]}), luminosity: {stars[i]["luminosity"]}, mass: {stars[i]["mass"]}")
    total_mass_list_1.append(stars[i]["mass"])
    total_mass_1 = total_mass_1 + stars[i]["mass"]

average_mass_1 = total_mass_1/len(total_mass_list_1)
print(total_mass, average_mass_1) #changes by 1.0204

user_wants_star = input("What star do you want to look up?").strip().title()

if user_wants_star not in stars.keys():
    print("star not found")
    user_wants_star = input("Input a different star")
else:
    print(stars[user_wants_star])

observation_log = [
    {"Star" : "Sirius", "Night" : 1, "Clear Sky" : False},
    {"Star" : "Buzz", "Night" : 2, "Clear Sky" : False},
    {"Star" : "Proxima Centauri", "Night" : 3, "Clear Sky" : True}
]

for e in range(len(observation_log)):
    print(f"Star: {observation_log[e]["Star"]}, Night: {observation_log[e]["Night"]}, Clear Sky: {observation_log[e]["Clear Sky"]}, Mass: {stars[observation_log[e]["Star"]]["mass"]}")