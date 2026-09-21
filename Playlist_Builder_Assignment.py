playlist = ["And Then is Heard No More", "Poems of a Machine", "Salt, Pepper, Birds, and the Thought Police", "Hero"]
new_Song = input("Add another song to this list.").title().strip()
playlist.append(new_Song)

print(playlist, new_Song)

print(len(playlist))

playlist.insert(0, "Saikai")
print(playlist)

removed_Song = playlist.pop(1)
print(removed_Song)

del playlist[3]

print(sorted(playlist))
playlist.sort(), playlist.reverse()

print("Camellia" in playlist)

for x in playlist:
    print(x.upper())

for i in range(len(playlist)):
    print(i + 1, playlist[i])