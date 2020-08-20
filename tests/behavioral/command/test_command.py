import pytest

from behavioral.command import TurnOnComputer, TurnOffComputer, RemoveVirus, Antivirus, ComputerCommands, Computer


class TestCommand:
    def test_it_creates_simple_commands(self):
        computer = Computer()
        commands = ComputerCommands()

        commands.register('on', TurnOnComputer(computer))
        commands.register('off', TurnOffComputer(computer))

        commands.execute('on')
        assert computer.get_power() is True

        commands.execute('off')
        assert computer.get_power() is False

    def test_it_creates_complex_command(self):
        computer = Computer()
        antivirus = Antivirus()
        commands = ComputerCommands()

        commands.register('on', TurnOnComputer(computer))
        commands.register('remove_virus', RemoveVirus(antivirus, computer))

        commands.execute('on')
        commands.execute('remove_virus')
        assert computer.get_number_virus() == 0
        assert computer.get_number_removed_files() == 0

    def test_it_can_not_remove_virus_with_computer_off(self):
        computer = Computer()
        antivirus = Antivirus()
        commands = ComputerCommands()

        commands.register('remove_virus', RemoveVirus(antivirus, computer))

        commands.execute('remove_virus')
        assert computer.get_number_virus() == 10
        assert computer.get_number_removed_files() == 10

    def test_it_raises_exception_if_command_not_registered(self):
        with pytest.raises(ValueError):
            commands = ComputerCommands()
            commands.execute('not_registered')

