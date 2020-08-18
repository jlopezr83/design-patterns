import abc


class MapSite(metaclass=abc.ABCMeta):
    """
    common abstract class for all the components of a maze
    """
    def enter(self):
        """
        :return: True if it's possible to enter, else False
        """
        pass


class Wall(MapSite):
    def __init__(self):
        self._color = 'white'

    def enter(self):
        return False


class Door(MapSite):
    def __init__(self, room1, room2, is_open=True):
        self._room1 = room1
        self._room2 = room2
        self._is_open = is_open
        self._color = 'white'

    def enter(self):
        return True if self._is_open else False


class Room(MapSite):
    def __init__(self, room_id):
        self._id = room_id
        self._sides = {}
        self._color = 'white'

    def enter(self):
        return False

    def get_id(self):
        return self._id

    def set_side(self, direction, map_site):
        self._sides[direction] = map_site

    def get_side(self, direction):
        return self._sides[direction]


class Maze:
    def __init__(self):
        self._rooms = {}

    def add_room(self, room):
        self._rooms[room.get_id()] = room

    def get_room(self, room_id):
        return self._rooms[room_id]

    def get_rooms(self):
        return self._rooms


class EnchantedRoom(Room):
    def __init__(self, room_id):
        super().__init__(room_id)
        self._color = 'black'


class DoorNeedingSpell(Door):
    def __init__(self, room1, room2, is_open=True):
        super().__init__(room1, room2, is_open)
        self._color = 'black'

