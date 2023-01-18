def are_you_playing_banjo(name):
    if name.lower().startswith("r"):
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"

name = input("What's your name? ")
print(are_you_playing_banjo(name))
