from abc import ABCMeta, abstractmethod


class AmericanPlugInterface(metaclass=ABCMeta):
    """
    Adaptee. Defines an existing interface that needs adapting.
    """
    @abstractmethod
    def voltage(self):
        pass

    @abstractmethod
    def live(self):
        pass

    @abstractmethod
    def neutral(self):
        pass


class AmericanPlug(AmericanPlugInterface):
    """
    Especific Adaptee
    """
    def voltage(self):
        return 110

    def live(self):
        return 1

    def neutral(self):
        return -1


class EuropeanPlugInterface(metaclass=ABCMeta):
    """
    Target. Defines the domain-specific interface that Client uses
    """
    @abstractmethod
    def voltage(self):
        pass

    @abstractmethod
    def live(self):
        pass

    @abstractmethod
    def neutral(self):
        pass

    @abstractmethod
    def earth(self):
        pass


class AmericanToEuropeanPlug(AmericanPlugInterface, EuropeanPlugInterface):
    """
    Adapter from American to European plug
    """
    def __init__(self, european_plug):
        self._european_plug = european_plug

    def voltage(self):
        return 220

    def live(self):
        self._european_plug.live()

    def neutral(self):
        self._european_plug.neutral()

    def earth(self):
        return 0


class Boiler:
    """
    Client class
    """
    def __init__(self, plug):
        self._plug = plug

    def boil(self):
        if self._plug.voltage() == 220:
            return True
        else:
            return False

