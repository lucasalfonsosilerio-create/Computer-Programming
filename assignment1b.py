# Silerio, Lucas
# Computer Programming, Period 4
# Assignment: Homework 2
# 31 August 2026

fav_hobby = "Video Games"
personal_message = "colin"
famous_person = "Albert Einstein"
famous_quote = "I have no special talent, I am only passionately curious."

print("I love", fav_hobby.lower())
print("Hello,", personal_message.title(), "I hope you are doing well.")
print(personal_message.lower(),personal_message.upper(), personal_message.title())

print(famous_person, "once said,", f'"{famous_quote}"')

message = f'{famous_person} once said, "{famous_quote}"'

print(message)

name2 = " Emilia "
print(f"{name2}\n{name2.lstrip()}\n{name2.rstrip()}\n{name2.strip()}")

filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

print(f"{11+0}\n{11-0}\n{11*1}\n{11/1}\n{11//1}")

favnumber = 5
print("My favorite number is", favnumber)