from Classes.Classes import *

# print welcome message
# print lore
# character creation:

def main():
    print("lore, backstory, etc...")
    print("who are you?")
    warrior_class = PlayerClass(1, "Warrior", None, None, "Sword")
    mage_class = PlayerClass(2, "Mage", None, None, "staff")
    rogue_class = PlayerClass(3, "Rogue", None, None, "Dagger")

    warrior = Character(1, None, warrior_class)
    mage = Character(2, None, mage_class)
    rogue = Character(2, None, rogue_class)

    characters = [warrior, mage, rogue]
    chosen_character = choose_character(characters)
    chosen_character.name = input("Name and occupation? (without the occupation): ")
    print(f"This you? {chosen_character.name} ({chosen_character.player_class.type})")
if __name__ == "__main__":
    main()
