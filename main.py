from Classes.Classes import *


def main():
    """The main function of the game."""
    # Character creation function
    def choose_character(character):
        """Choose a character from a list of available characters.

        Args:
            character (list): List of available characters.

        Returns:
            Character: The chosen character.
        """
        print("Available Classes:")
        for index, character in enumerate(character):
            print(f"{index + 1}. ({character.player_class.type})")

        while True:
            choice = input("Choose a character by entering its number: ")
            try:
                choice = int(choice)
                if 1 <= choice <= len(character):
                    return character[choice - 1]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Map settings
    map_height = 5
    map_width = 5
    game_map = GameMap(1, map_width, map_height)
    game_map.shuffle_tiles()

    # Set encounters
    game_map.set_encounter(2, 2, Encounter(1, "Enemy", "Orc!", ""))
    game_map.set_encounter(4, 4, Encounter(2, "Enemy", "Goblin!", ""))

    # Define stats for different classes
    warrior_stats = {'max_health': 8, 'health': 8, 'defense': 4, 'dodge': 1, 'attack': 3, 'max_mana': 1, 'mana': 1}
    mage_stats = {'max_health': 4, 'health': 4, 'defense': 1, 'dodge': 3, 'attack': 2, 'max_mana': 7, 'mana': 7}
    rogue_stats = {'max_health': 4, 'health': 4, 'defense': 1, 'dodge': 7, 'attack': 4, 'max_mana': 1, 'mana': 1}

    print("lore, backstory, etc...")
    print("Who are you?")

    # Character creation
    warrior_class = PlayerClass(1, "Warrior", warrior_stats, {}, "Sword")
    mage_class = PlayerClass(2, "Mage", mage_stats, {}, "Staff")
    rogue_class = PlayerClass(3, "Rogue", rogue_stats, {}, "Dagger")

    warrior = Character(1, "", warrior_class)
    mage = Character(2, "", mage_class)
    rogue = Character(2, "", rogue_class)

    characters = [warrior, mage, rogue]
    chosen_character = choose_character(characters)
    chosen_character.name = input("Name: ")

    # Display chosen character and their stats
    print(f"This you? \n{chosen_character}")
    for stat, value in chosen_character.player_class.stats.items():
        print(f"{stat.capitalize()}: {value}")

    current_location = (0, 0)

    while True:
        print(f"You are at location {current_location}")
        direction = input("Enter direction (up, down, right, left): ")
        new_location = current_location

        # Navigation
        if direction in ["up", "down", "right", "left"]:
            if direction == "up" and current_location[1] < map_height - 1:
                new_location = (current_location[0], current_location[1] + 1)
            elif direction == "down" and current_location[1] > 0:
                new_location = (current_location[0], current_location[1] - 1)
            elif direction == "right" and current_location[0] < map_width - 1:
                new_location = (current_location[0] + 1, current_location[1])
            elif direction == "left" and current_location[0] > 0:
                new_location = (current_location[0] - 1, current_location[1])
            else:
                print("Out of bounds.")
        else:
            print("Enter a valid direction.")

        if new_location != current_location:
            current_location = new_location

        # Check for encounter
        encounter = game_map.get_encounter(*current_location)
        if encounter:
            print(f"Encounter: You encountered a {encounter.enemy}")


if __name__ == "__main__":
    main()
