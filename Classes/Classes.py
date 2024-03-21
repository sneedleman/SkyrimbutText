class Character():
    def __init__(self, ID, name, playerClass):
        self._ID = ID
        self._name = name
        self._playerClass = playerClass
        self._items = []


class PlayerClass():
    def __init__(self, ID, type, stats, attributes, weaponType):
        self._ID = ID
        self._type = type
        self._stats = stats
        self._attributes = attributes
        self._weaponType = weaponType


class WeaponType():
    def __init__(self, ID, type, damage, description):
        self._id = ID
        self._type = type
        self._damage = damage
        self._description = description

        @property
        def type(self):
            return self._type
        
        @type.setter
        def set_type(self, value):
            sel
            pass

class Stats():
    def __init__(self, ID, maxHealth, health, defense, maxMana, mana):
        self._id = ID
        self._type = type
        self._maxHealth = maxHealth
        self._health = health
        self._defense = defense
        self._maxMana = maxMana
        self._mana = mana

