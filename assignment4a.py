# Silerio, Lucas
# Computer Programming, period 4
# Assignment: Homework 4a
# Oct 27, 2027

person = {
    "first name" : "chad",
    "last name" : "mcneel",
    "age" : "18",
    "city" : "los angeles"
}

for i,v in person.items():
    print(i)
    print(v)

aboutMe = {
    "name" : "lucas", 
    "age" : 17,
    "fav food" : ["fries", "chips", "burger", "cookies", "ice cream"],
    "hair color" : "black",
    "fav subject" : "senior magis",
    "fav sweet" : "chocolate ice cream",
    "fav hobbies" : ["video games", "playing with the dog", "talking with friends"],
    "likeCoding" : True
}

print(aboutMe)

phoneBook = {
    "John" : 938477566,
    "Jack" : 93877264,
    "Jill" : 947662781,
}

jill = phoneBook.pop("Jill")
print(phoneBook)
print(jill)

glossary = {
    "servant leader" : "leader who serves others",
    "instrumental value of ethic" : "ways to act",
    "terminal value of ethic" : "goals",
    "six stages of moral development" : "preconventional, conventional, then postcovential",
    "creativity" : "core of being a leader"
}

print(f"servant leader : {glossary['servant leader']}\n")
print(f"instrumental value of ethic : {glossary['instrumental value of ethic']}\n")
print(f"terminal value of ethic : {glossary['terminal value of ethic']}\n")
print(f"six stages of moral development : {glossary['six stages of moral development']}\n")
print(f"creativity : {glossary['creativity']}\n")

glossary[".items()"] = "gets every item in a dictionary"
glossary[".pop()"] = "removes an item from a list or dictionary"
glossary[".keys()"] = "gets all keys from a dictionary"
glossary[".values()"] = "gets all values from a dictionary"
glossary["bool value"] = "can be true or false"

for i, v in glossary.items():
    print(f"{i} means {v}\n")

rivers = {
    "nile" : "egypt",
    "amazon" : "peru",
    "mississippi" : "united states",
    "yangtze" : "china",
    "missouri" : "united states"
}

for k, v in rivers.items():
    print(k, v)
    print(f"the {k} runs through the {v}\n")

people = [
    {
        "first name" : "chad",
        "last name" : "mcneel",
        "favorite color" : "green",
        "birth month" : "april"
    },
    {
        "first name" : "emilia",
        "last name" : "silerio",
        "favorite color" : "blue",
        "birth month" : "april"
    },
    {
        "first name" : "jackson",
        "last name" : "thimes",
        "favorite color" : "yellow",
        "birth month" : "july"
    }
]

for x in people:
    print(F"{x}\n")

UScities = {
    "los angeles" : {
        "state" : "california",
        "rough population" : 3870000,
        "fact" : "entertainment capital of the world"
    },
    "las vegas" : {
        "state" : "nevada",
        "rough population" : 679817,
        "fact" : "named after hidden underground wells"
    },
    "new york city" : {
        "state" : "new york",
        "rough population" : 8586038,
        "fact" : "more than 800 languages are spoken here"

    }
}

for r, p in UScities.items():
    print(f"city {r} has {p}\n")