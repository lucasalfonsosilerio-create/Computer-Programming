# Silerio, Lucas
# Computer Programming, period 4
# Assignment: Homework 6
# Nov 16, 2027
default_message = "I love Python"
def make_shirt2(size, design):
    print(f"Your shirt's size is {size} and its design is {design}")

make_shirt2("M", "skull")

def make_shirt(s):
    make_shirt2(s, "I love Python")

make_shirt("L")
make_shirt2("M", default_message)
make_shirt2("S", "hi")

def cityCountry(city, country):
    print(f"{city}, {country}")

cityCountry("LA", "United States")
cityCountry("Manilla", "Phillipines")
cityCountry("Mumbai", "India")

def make_album(name, title, songs=None):
    album = {
        "album artist" : name,
        "album title" : title
    }

    if songs is not None:
        album["album songs"] = songs
    else:
        album["album songs"] = 1
    return(album)

album1 = make_album("Mili", "Key Ingredient", 13)
print(album1)

album2 = make_album("Pink Floyd", "Dark Side of the Moon")
print(album2)

album3 = make_album("Flavor Foley", "Mirror Modulation", 6)
print(album3)

while True:
    x = input("Artist of album: ").title().strip()
    y = input("Name of album: ").title().strip()

    album = make_album(x,y)
    print(album)

    anymore = input("Anymore albums? ").strip().title()

    if anymore.lower().startswith("n"):
        break

messages = ["hi", "hi lol", "image.png", "XD", "peepee poopoo"]
copy_messages = ["hi", "hi lol", "image.png", "XD", "peepee poopoo"]

def show_messages():
    sent_messages = []

    while len(messages) > 0:
        current = messages.pop()
        sent_messages.append(current)

    sent_messages.reverse()

    print(sent_messages, messages)

show_messages()
print(copy_messages)

def sandwiches(x):
    sandwichList = []
    runtimes = x
    while runtimes > 0: 
        sandwichOrder = input("What sandwich you want? ").strip()
        sandwichList.append(sandwichOrder)
        print(sandwichList)
        runtimes -= 1

sandwiches(1)
sandwiches(2)
sandwiches(3)

def car(manufacturer, modelNum, **details):
    details["manufacturer"] = manufacturer
    details["model"] = modelNum

    print(details)

carModel = car('subaru','outback',color='blue',tow_package=True)

from assignment6sup import HelloWorld

HelloWorld(3)