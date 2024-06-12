import json
from Classes.Classes import *


def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def create_player_class(class_data):
    return PlayerClass(
        class_data['ID'],
        class_data['type'],
        class_data['stats'],
        class_data['attributes'],
        class_data['weapon_type']
    )


def create_item(item_data):
    return {
        'ID': item_data['ID'],
        'name': item_data['name'],
        'description': item_data['description']
    }


def get_map_size():
    while True:
        map_size = input("Choose map size: small, medium, big: ").lower()
        if map_size == "small":
            return 5, 5
        elif map_size == "medium":
            return 10, 10
        elif map_size == "big":
            return 15, 15
        else:
            print("Invalid input. Please enter 'small', 'medium', or 'big'.")


def main():
    try:
        # Get map size from user
        map_width, map_height = get_map_size()
        game_map = GameMap(1, map_width, map_height)
        game_map.shuffle_tiles()

        encounters = load_json('encounters.json')['encounters']
        encounter_positions = random.sample([(x, y) for x in range(map_width) for y in range(map_height)],
                                            len(encounters))

        for position, encounter_data in zip(encounter_positions, encounters):
            encounter = Encounter(
                encounter_data['ID'],
                encounter_data['encounter_type'],
                encounter_data['description'],
                encounter_data['dialog'],
                encounter_data.get('reward')
            )
            game_map.set_encounter(position[0], position[1], encounter)

        classes = load_json('classes.json')['classes']
        warrior_class = create_player_class(classes[0])
        mage_class = create_player_class(classes[1])
        rogue_class = create_player_class(classes[2])

        print("lore, backstory, etc...")
        print("Who are you?")

        warrior = Character(1, "", warrior_class)
        mage = Character(2, "", mage_class)
        rogue = Character(3, "", rogue_class)

        def choose_character(characters):
            try:
                print("Available Classes:")
                for index, character in enumerate(characters):
                    print(f"{index + 1}. ({character.player_class.type})")

                while True:
                    choice = input("Choose a character by entering its number: ")
                    try:
                        choice = int(choice)
                        if 1 <= choice <= len(characters):
                            return characters[choice - 1]
                        else:
                            print("Invalid choice. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            except Exception as e:
                print(f"Error during character selection: {e}")
                return None

        characters = [warrior, mage, rogue]
        chosen_character = choose_character(characters)
        if chosen_character:
            chosen_character.name = input("Name: ")

            print(f"This you? \n{chosen_character}")
            for stat, value in chosen_character.player_class.stats.items():
                print(f"{stat.capitalize()}: {value}")

            current_location = (0, 0)

            while True:
                print(f"You are at location {current_location}")
                direction = input("Enter direction (up, down, right, left): ")
                new_location = current_location

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

                encounter = game_map.get_encounter(*current_location)
                if encounter:
                    print(f"{encounter.dialog}")
                    if encounter.reward:
                        chosen_character.add_item(encounter.reward)
                        print(f"You received: {encounter.reward['name']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
