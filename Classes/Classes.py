import random


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

    def __str__(self):
        return f"Name: {self._name}, Class: {self._player_class.type}"

    def add_item(self, item):
        self._items.append(item)
        print(f"Added {item['name']} to inventory.")

    def remove_item(self, to_be):
        for item in self._items:
            if item['name'] == to_be:
                self._items.remove(item)
                print(f"Item '{to_be}' removed from inventory.")
                return
        print(f"Item '{to_be}' not found in inventory.")

    def view_inventory(self):
        if not self._items:
            print("broke ahh")
        else:
            print("Inventory: \n")
            for item in self._items:
                print(f"- {item['name']}")


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
    def __init__(self, ID, max_health, health, defense, dodge, attack, max_mana, mana):
        self._ID = ID
        self._max_health = max_health
        self._health = health
        self._defense = defense
        self._dodge = dodge
        self._attack = attack
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


class Inventory:
    def __init__(self, ID, Name, Type, Defense, Effect, Description):
        self._ID = ID
        self._Name = Name
        self._Type = Type
        self._Defense = Defense
        self._Effect = Effect
        self._Description = Description

    def add_item(self):
        pass

    def remove_item(self):
        pass

    def display_items(self):
        pass


class GameMap:
    def __init__(self, ID, width, height):
        self._ID = ID
        self._width = width
        self._height = height
        self._map_data = [[None] * width for _ in range(height)]
        self._encounters = {}

        self._initialize_map()

    def _initialize_map(self):
        counter = 1
        for y in range(self._height):
            for x in range(self._width):
                self._map_data[y][x] = Tile(counter)
                counter += 1

    def shuffle_tiles(self):

        start_tile = self._map_data[self._height - 1][0]
        end_tile = self._map_data[0][self._width - 1]

        flattened_map = [tile for row in self._map_data for tile in row if tile not in [start_tile, end_tile]]

        random.shuffle(flattened_map)

        # Reassign the shuffled tiles back to the map
        counter = 0
        for y in range(self._height):
            for x in range(self._width):
                if (x, y) == (0, 0):
                    self._map_data[y][x] = start_tile  # Set start tile back to its original position
                elif (x, y) == (self._width - 1, self._height - 1):
                    self._map_data[y][x] = end_tile  # Set end tile back to its original position
                else:
                    self._map_data[y][x] = flattened_map[counter]  # Set the shuffled tile
                    counter += 1

    @property
    def ID(self):
        return self._ID

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def map_data(self):
        return self._map_data

    def print_map(self):
        for row in self.map_data:
            print(row)

    def set_tile(self, x, y, tile):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.map_data[y][x] = tile
        else:
            print("Out of bounds.")

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.map_data[y][x]
        else:
            print("Out of bounds.")
            return None

    def set_encounter(self, x, y, encounter):
        if 0 <= x < self._width and 0 <= y < self._height:
            self._encounters[(x, y)] = encounter
        else:
            print("Out of bounds.")

    def get_encounter(self, x, y):
        return self._encounters.get((x, y), None)


class Tile:
    def __init__(self, ID):
        self._ID = ID

    @property
    def ID(self):
        return self._ID

    def __str__(self):
        return str(self._ID)


class Encounter:
    def __init__(self, ID, encounter_type, description, dialog, reward=None):
        self._ID = ID
        self._encounter_type = encounter_type
        self._description = description
        self._dialog = dialog
        self._reward = reward

    @property
    def ID(self):
        return self._ID

    @property
    def encounter_type(self):
        return self._encounter_type

    @property
    def description(self):
        return self._description

    @property
    def dialog(self):
        return self._dialog

    @property
    def reward(self):
        return self._reward

    def __str__(self):
        return f"Encounter: {self._description}, Dialog: {self._dialog}, Reward: {self._reward}"
