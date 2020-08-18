import abc

from creational.common.mazes import Maze, Wall, Room, EnchantedRoom, Door, DoorNeedingSpell


class MazeGame:
    @staticmethod
    def create_maze(maze_factory):
        maze = maze_factory.make_maze()

        room1 = maze_factory.make_room(1)
        room2 = maze_factory.make_room(2)

        door = maze_factory.make_door(room1, room2)

        room1.set_side('North', maze_factory.make_wall())
        room1.set_side('East', door)
        room1.set_side('South', maze_factory.make_wall())
        room1.set_side('West', maze_factory.make_wall())
        room2.set_side('North', maze_factory.make_wall())
        room2.set_side('East', maze_factory.make_wall())
        room2.set_side('South', maze_factory.make_wall())
        room2.set_side('West', door)

        maze.add_room(room1)
        maze.add_room(room2)

        return maze


class AbstractMazeFactory(metaclass=abc.ABCMeta):
    """
    Abstract factory to create different types of mazes
    """
    @abc.abstractmethod
    def make_maze(self):
        pass

    @abc.abstractmethod
    def make_wall(self):
        pass

    @abc.abstractmethod
    def make_room(self, room_id):
        pass

    @abc.abstractmethod
    def make_door(self, room1, room2):
        pass


class MazeFactory(AbstractMazeFactory):
    """
    Concrete factory to create normal mazes
    """
    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_room(self, room_id):
        return Room(room_id)

    def make_door(self, room1, room2):
        return Door(room1, room2)


class EnchantedMazeFactory(AbstractMazeFactory):
    """
    Concrete factory to create enchanted mazes
    """
    def make_maze(self):
        return Maze()

    def make_wall(self):
        return Wall()

    def make_room(self, room_id):
        return EnchantedRoom(room_id)

    def make_door(self, room1, room2):
        return DoorNeedingSpell(room1, room2)



