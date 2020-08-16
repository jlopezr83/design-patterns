import abc


class Command(metaclass=abc.ABCMeta):
    """
    Interface for executing an operation
    """
    @abc.abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    """
    Concrete command to turn on the computer
    """
    def __init__(self, computer):
        self._computer = computer

    def execute(self):
        self._computer.turn_on()


class TurnOffCommand(Command):
    """
    Concrete command to turn off the computer
    """
    def __init__(self, computer):
        self._computer = computer

    def execute(self):
        self._computer.turn_off()


class ComplexCommand(Command):
    """
    Concrete command to execute some complex operations. It defines a binding between a Receiver object and an action
    """
    def __init__(self, receiver, computer):
        self._receiver = receiver
        self._computer = computer

    def execute(self):
        self._receiver.operation1(self._computer)
        self._receiver.operation2(self._computer)


class Invoker:
    """
    Invoker. It asks the command to carry out the request
    """
    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name not in self._commands:
            raise ValuError(f'No command {command_name} registered')

        self._commands[command_name].execute()


class Receiver:
    """
    Receiver. It knows how to perform the operations associated with carrying out a request
    """
    def operation1(self, computer):
        computer.increase_counter()

    def operation2(self, computer):
        computer.duplicate_counter()


class Computer:
    def __init__(self):
        self._power = False
        self._counter = 0

    def turn_on(self):
        self._power = True

    def turn_off(self):
        self._power = False

    def get_power(self):
        return self._power

    def get_counter(self):
        return self._counter

    def increase_counter(self):
        self._counter += 1

    def duplicate_counter(self):
        self._counter *= 2