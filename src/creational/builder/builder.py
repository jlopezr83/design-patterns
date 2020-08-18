from abc import ABCMeta, abstractmethod

from creational.common.mazes import Maze, Room, Door, Wall


class MazeGame:
    @staticmethod
    def create_maze(maze_builder):
        maze_builder.build_maze()
        maze_builder.build_room(1)
        maze_builder.build_room(2)
        maze_builder.build_door(1, 2)

        return maze_builder.get_maze()

    @staticmethod
    def create_complex_maze(maze_builder):
        maze_builder.build_maze()
        maze_builder.build_room(1)
        maze_builder.build_room(2)
        maze_builder.build_door(1, 2)
        maze_builder.build_room(3)
        maze_builder.build_door(2, 3)

        return maze_builder.get_maze()


class MazeBuilder(metaclass=ABCMeta):
    def __init__(self):
        self._maze = None

    @abstractmethod
    def build_maze(self):
        pass

    @abstractmethod
    def build_room(self, room_id):
        pass

    @abstractmethod
    def build_door(self, room1, room2):
        pass

    def get_maze(self):
        return self._maze


class StandardMazeBuilder(MazeBuilder):
    def build_maze(self):
        self._maze = Maze()

    def build_room(self, room_id):
        if room_id in self.get_maze().get_rooms():
            return

        room = Room(room_id)
        room.set_side('North', Wall())
        room.set_side('East', Wall())
        room.set_side('South', Wall())
        room.set_side('West', Wall())

        self._maze.add_room(room)

    def build_door(self, room_id1, room_id2):
        room1 = self.get_maze().get_room(room_id1)
        room2 = self.get_maze().get_room(room_id2)

        door = Door(room1, room2)

        room1.set_side(self._common_wall(room1, room2), door)
        room2.set_side(self._common_wall(room2, room1), door)

    @staticmethod
    def _common_wall(room1, room2):
        return 'West' if room1.get_id() < room2.get_id() else 'East'


class CountingMazeBuilder(MazeBuilder):
    """
    This builder doesn't create a maze at all,
    it just counts the different kinds of components that would have been created.
    """
    def build_maze(self):
        self._maze = {
            'doors': 0,
            'rooms': 0
        }

    def build_room(self, room_id):
        self._maze['rooms'] += 1

    def build_door(self, room1, room2):
        self._maze['doors'] += 1
