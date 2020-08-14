import abc


class StringFormatter:
    """
    Abstraction
    """
    def __init__(self, formatter):
        self._formatter = formatter

    def format(self, string):
        return self._formatter.format(string)


class Formatter(metaclass=abc.ABCMeta):
    """
    Implementor
    """
    @abc.abstractmethod
    def format(self, string):
        pass


class FormatterLowerCase(Formatter):
    """
    Concrete Implementor
    """
    def format(self, string):
        return string.lower()


class FormatterUpperCase(Formatter):
    """
    Concrete Implementor
    """
    def format(self, string):
        return string.upper()
