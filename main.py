from Classes.Classes import *


def main():
    def choose_character(char):
        print("Available Classes:")
        for index, character in enumerate(char):
            print(f"{index + 1}. ({character.player_class.type})")

        while True:
            choice = input("Choose a character by entering its number: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(char):
                    return char[choice - 1]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    map_width = 3
    map_height = 3
    game_map = GameMap(1, map_width, map_height)
    current_location = (0, 0)
    game_map.set_encounter(2, 2, Encounter(1, "Orc", "dialog!"))
    game_map.set_encounter(4, 4, Encounter(1, "Goblin", "dialog!"))

    # stats:
    warrior_stats = {
        'max_health': 8,
        'health': 8,
        'defense': 4,
        'dodge': 1,
        'attack': 3,
        'max_mana': 1,
        'mana': 1
    }

    mage_stats = {
        'max_health': 4,
        'health': 4,
        'defense': 1,
        'dodge': 3,
        'attack': 2,
        'max_mana': 7,
        'mana': 7
    }

    rogue_stats = {
        'max_health': 4,
        'health': 4,
        'defense': 1,
        'dodge': 7,
        'attack': 4,
        'max_mana': 1,
        'mana': 1
    }

    print("lore, backstory, etc...")
    print("who are you?")

    # character creation
    warrior_class = PlayerClass(1, "Warrior", warrior_stats, None, "Sword")
    mage_class = PlayerClass(2, "Mage", mage_stats, None, "staff")
    rogue_class = PlayerClass(3, "Rogue", rogue_stats, None, "Dagger")

    warrior = Character(1, None, warrior_class)
    mage = Character(2, None, mage_class)
    rogue = Character(2, None, rogue_class)

    characters = [warrior, mage, rogue]
    chosen_character = choose_character(characters)
    chosen_character.name = input("Name: ")

    # this should work for now
    print(f"This you? \n{chosen_character}")
    for stat, value in chosen_character.player_class.stats.items():
        print(f"{stat.capitalize()}: {value}")
    while True:
        print(f"You are at location {current_location}")
        direction = input("Enter direction (up, down, right, left): ")
        if direction == "up":
            current_location = (current_location[0], current_location[1] - 1)
        elif direction == "down":
            current_location = (current_location[0], current_location[1] + 1)
        elif direction == "right":
            current_location = (current_location[0] + 1, current_location[1])
        elif direction == "left":
            current_location = (current_location[0] - 1, current_location[1])
        else:
            print("Invalid direction.")

        encounter = game_map.get_encounter(*current_location)
        if encounter:
            print(f"Encounter: You encountered a {encounter.enemy_type}!")


if __name__ == "__main__":
    main()
