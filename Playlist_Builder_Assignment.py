#STEP 1: Make the playlist
playlist = ["And Then is Heard No More", "Poems of a Machine", "Salt, Pepper, Birds, and the Thought Police", "Hero"]
new_Song = input("Add another song to this list.").title().strip()
#STEP 2: Insert new song
playlist.append(new_Song)

print(playlist, new_Song)

print(len(playlist))

#STEP 3: Insert new song
playlist.insert(0, "Saikai")
print(playlist)

#STEP 4: Removing songs
removed_Song = playlist.pop(1)
print(removed_Song)

del playlist[3]

#Step 5: Sorting the playlist
print(sorted(playlist))
playlist.sort(), playlist.reverse()

print("Camellia" in playlist)

#Step 6: Print all of the songs
for x in playlist:
    print(x.upper())

for i in range(len(playlist)):
    print(i + 1, playlist[i])