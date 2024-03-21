# print("welcome message")
# print lore
# character creation:
print("who are you?")


def create_character():
    attributes = {"strength": 0, "agility": 0, "intelligence": 0}
    total_points = 10
    print("you have 10 available skill points to allocate to your attributes")
    while total_points > 0:
        print("\nAttributes:\n")
        print("1. Strength: ", attributes['strength'])
        print("2. Agility: ", attributes['agility'])
        print("3. Intelligence: ", attributes['intelligence'])
        print("Points remaining: ", total_points)

        choice = input("Enter attribute you wish to increase \n")

        if choice not in attributes.keys():
            print("Please enter one of the available attributes.")
        else:
            print("How many points to invest in this attribute?")


create_character()
