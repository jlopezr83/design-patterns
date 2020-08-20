from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    """
    Interface for executing an operation
    """
    @abstractmethod
    def execute(self):
        pass


class TurnOnComputer(Command):
    """
    Concrete command to turn on the computer
    """
    def __init__(self, computer):
        self._computer = computer

    def execute(self):
        self._computer.turn_on()


class TurnOffComputer(Command):
    """
    Concrete command to turn off the computer
    """
    def __init__(self, computer):
        self._computer = computer

    def execute(self):
        self._computer.turn_off()


class RemoveVirus(Command):
    """
    Concrete complex command to remove the viruses. It defines a binding between a receiver and an action
    """
    def __init__(self, antivirus, computer):
        self._antivirus = antivirus
        self._computer = computer

    def execute(self):
        self._antivirus.remove_virus(self._computer)
        self._antivirus.clean(self._computer)


class Antivirus:
    """
    Receiver. It knows how to perform the operations associated with carrying out a request
    """
    @staticmethod
    def remove_virus(computer):
        computer.remove_virus()

    @staticmethod
    def clean(computer):
        computer.delete_trash()


class ComputerCommands:
    """
    Invoker. It asks the command to carry out the request
    """
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name not in self._commands:
            raise ValueError(f'No command {command_name} registered')

        self._commands[command_name].execute()


class Computer:
    """
    Class to store the status of the computer
    """
    def __init__(self, virus=0, removed_files=0):
        self._power = False
        self._virus = virus
        self._removed_files = removed_files

    def get_power(self):
        return self._power

    def get_number_virus(self):
        return self._virus

    def get_number_removed_files(self):
        return self._removed_files

    def turn_on(self):
        self._power = True

    def turn_off(self):
        self._power = False

    def remove_virus(self):
        if not self._power:
            return

        self._virus = 0

    def delete_trash(self):
        if not self._power:
            return

        self._removed_files = 0
