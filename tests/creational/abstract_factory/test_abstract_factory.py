from creational.abstract_factory import MazeGame, MazeFactory, EnchantedMazeFactory
from creational.common.mazes import Room, EnchantedRoom


class TestAbstractFactory:
    def test_it_creates_maze(self):
        maze = MazeGame.create_maze(MazeFactory())
        for room_id, room in maze.get_rooms().items():
            assert isinstance(room, Room)

    def test_it_creates_enchanted_maze(self):
        enchanted_maze = MazeGame.create_maze(EnchantedMazeFactory())
        for room_id, room in enchanted_maze.get_rooms().items():
            assert isinstance(room, EnchantedRoom)


