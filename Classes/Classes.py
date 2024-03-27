class Character:
    def __init__(self, ID, name, player_class):
        self._ID = ID
        self._name = name
        self._player_class = player_class
        self._items = []

    @property
    def ID(self):
        return self._ID

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def player_class(self):
        return self._player_class

    @property
    def items(self):
        return self._items



class PlayerClass:
    def __init__(self, ID, type, stats, attributes, weapon_type):
        self._ID = ID
        self._type = type
        self._stats = stats
        self._attributes = attributes
        self._weapon_type = weapon_type

    @property
    def ID(self):
        return self._ID

    @property
    def type(self):
        return self._type

    @property
    def stats(self):
        return self._stats

    @property
    def attributes(self):
        return self._attributes

    @property
    def weapon_type(self):
        return self._weapon_type


class WeaponType:
    def __init__(self, ID, type, damage, description):
        self._ID = ID
        self._type = type
        self._damage = damage
        self._description = description

    @property
    def ID(self):
        return self._ID

    @property
    def type(self):
        return self._type

    @property
    def damage(self):
        return self._damage

    @property
    def description(self):
        return self._description


class Stats:
    def __init__(self, ID, max_health, health, defense, max_mana, mana):
        self._ID = ID
        self._max_health = max_health
        self._health = health
        self._defense = defense
        self._max_mana = max_mana
        self._mana = mana

    @property
    def ID(self):
        return self._ID

    @property
    def max_health(self):
        return self._max_health

    @property
    def health(self):
        return self._health

    @property
    def defense(self):
        return self._defense

    @property
    def max_mana(self):
        return self._max_mana

    @property
    def mana(self):
        return self._mana

def choose_character(characters):
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
