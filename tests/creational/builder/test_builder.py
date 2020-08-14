from creational.builder import MazeGame, StandardMazeBuilder, CountingMazeBuilder


class TestBuilder:
    def test_it_creates_standard_maze(self):
        maze = MazeGame().create_maze(StandardMazeBuilder())
        assert len(maze.get_rooms()) == 2

    def test_it_creates_standard_complex_maze(self):
        maze = MazeGame().create_complex_maze(StandardMazeBuilder())
        assert len(maze.get_rooms()) == 3

    def test_it_counts_elements_maze(self):
        maze = MazeGame().create_maze(CountingMazeBuilder())
        assert maze['rooms'] == 2
        assert maze['doors'] == 1

    def test_it_counts_elements_complex_maze(self):
        maze = MazeGame().create_complex_maze(CountingMazeBuilder())
        assert maze['rooms'] == 3
        assert maze['doors'] == 2
