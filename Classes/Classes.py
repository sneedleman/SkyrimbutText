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


class GameMap:
    def __init__(self, ID, width, height):
        self._ID = ID
        self._width = width
        self._height = height
        self._map_data = [[None] * width for _ in range(height)]

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

    #   Methods:
    #       - __init__(width, height): constructor method to initialize the map with given dimensions
    #       - print_map(): method to print the map to the console
    #       - set_tile(x, y, tile): method to set the value of a specific tile on the map
    #       - get_tile(x, y): method to get the value of a specific tile on the map

    #   Method to print the map:
    def print_map(self):
        for row in self.map_data:
            print(row)

    #   Method to set a tile value:
    def set_tile(self, x, y, tile):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.map_data[y][x] = tile
        else:
            print("Error: Out of bounds.")

    #   Method to get a tile value:
    # Function get_tile(x, y):
    def get_tile(self, x, y):
        # If 0 <= x < self.width and 0 <= y < self.height:
        if 0 <= x < self.width and 0 <= y < self.height:
            # Return the value of self.map_data[y][x]
            return self.map_data[y][x]
        # Else:
        else:
            # Print an error message indicating out of bounds
            print("Error: Out of bounds")
            # Return None
            return None
