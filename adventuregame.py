# Silerio, Lucas
# Computer Programming, Period 4
# Assignment: Homework 2
# 6 October 2026

print("you wake up in a dark and scary house that you've never been in, two rooms are avaliable for you\n")

direction = input("would you like to turn right or left\n")

if direction.strip().lower() == "left":
    x = input("oh god im scared im in a dark room, will you investigate the corner or investigate the table\n")

    if x.strip().lower() == "corner":
        print("you walk into a secret passageway, but the wall closes behind you\n")
        x = input("there's two directions, go left or right\n")

        if x.strip().lower().startswith("left"):
            print("you stumble into a dungeon, with two doors, but they speak, the first door says 'Go left, that one will lead you to freedom', the other says 'No, go right, that one will lead you to freedom.'\n")
            x = input("will you go through the first or second door will you go through\n")

            if x.strip().lower().startswith("first"):
                print("through the first door, you stumble into yet another crossroads\n")
                x = input("will you go left or right\n")

                if x.strip().lower().startswith("left"):
                    print("you end up walking onto a pressure plate\n")

                elif x.strip().lower().startswith("right"):
                    print("you end up in a room with a problem is on the wall 'what's 6x + 10 = 46'\n")
                    x = int(input("what's the answer for the problem on the wall (number)\n").strip().lower())

                    if x == 6:
                        print("the door opens and sunshine comes pouring in, you've escaped!\n")
                    elif x != 6:
                        print("the ceiling falls in on you and you die\n")

            elif x.strip().lower().startswith("second"):
                print("you fall to your untimely demise\n")

        elif x.strip().lower() == "right":
            print("in this passageway you see yet two more ways to go, this passageway seems relatively safe\n")
            x = input("will you go forward or left\n")

            if x == "left":
                print("you end up finding an old door, opening it reveals the outside world, you're free!\n")

            elif x == "forward":
                print("you end up going forward, and end up in a room filled with various devices\n")
                x = input("there seems to be two doors, will you go to the right or left\n")
                if x == "left":
                    print("upon opening the left door, it activates some of the traps and you end up dying because of it\n")
                elif x == "right":
                    print("upon opening the right door, nothing happens, but you find your way out of the place you were in, you're free\n")
    elif x.strip().lower() == "table":
        print("suddenly, you're sucked into the hole that was under the table, and after getting up you see two paths\n")
        x = input("there's two directions, go right or forward\n")

        if x.strip().lower().startswith("right"):
            print("going right reveals a kitchen of sorts\n")
            x = input("from here, you can see you can go through the window or the door\n")
        
            if x.strip().lower().startswith("window"):
                print("through the window, you stumble into a small room\n")
                x = input("there's two doors on your right and left, which direction will you go\n")
        
                if x.strip().lower().startswith("left"):
                    print("you end up walking into a room that drops an anvil on your head, you die\n")
        
                elif x.strip().lower().startswith("right"):
                    print("from this door, you are able to escape safely and soundly\n")

            elif x.strip().lower().startswith("door"):
                print("going through the door you end up in a restaurant and you're forced to work there for the rest of your life\n")
        
        elif x.strip().lower() == "forward":
            print("you enter a somewhat dark and damp passageway\n")
            x = input("will you go forward or left\n")
        
            if x == "left":
                print("you end up walking for hours, but eventually, you find your way out into the forest, you're free!\n")
        
            elif x == "forward":
                print("you end up going forward, and end up in another crossroads\n")
                x = input("there seems to be two paths, will you go to the left or forward\n")
                if x == "left":
                    print("upon going left, you stumble into a room with a hole in the middle and a door to your right\n")
                    x = input("jump or right\n")

                    if x == "jump":
                        print("surprisingly, you land on grass, you're free!\n")
                    elif x == "right":
                        print("you end up walking into a room full of spikes, and the walls close in on you, ending you\n")
                elif x == "forward":
                    print("going forwards presents an endless hallway, you're trapped forever\n")
    else:
        print("your indecisiveness gets you killed\n")
elif direction.strip().lower() == "right":
    print("you actually end up in the bathroom\n")
    x = input("will you investigate the toliet or the window\n")

    if x == "toliet":
        print("upon looking in the toliet, you are sucked into the toliet by a monster, ultimately causing you to die\n")
    elif x == "window":
        print("upon looking at the window, you realize the window is unlocked, and you climb through to freedom\n")
    else:
        print("your indecisiveness gets you killed\n")