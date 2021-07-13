# Create a function that allows someone to guess the value of any key in the dictionary, and find out if
# they were right or wrong. This function should accept two parameters: Key and Value. If the key
# exists in the dictionary and that value is the correct value, then the function should return true. In all
# other cases, it should return false.
favorite_song = {
       "genre": "bongo",
        "Artist": "Alikiba",
        "Duration": 3.55,
        "Year Of Release": 2019,
        "Song": "Mshumaah",

}
for key, value in favorite_song.items():
    print(key, value)

print()


def guess_music():

    while True:
        key = input("enter key: ")
        if key in favorite_song:
            value = input("enter its value: ")
            if value not in favorite_song[key]: # value of the key from the dictionary
                print("Your value is not correct")
                break
            else:
                print("CONGRATULATION YOU WON")
                break
        else:
            if key not in favorite_song:
                print("wrong key")
            break


guess_music()


