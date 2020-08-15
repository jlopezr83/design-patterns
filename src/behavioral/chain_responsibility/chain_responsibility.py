import abc


class Request:
    def __init__(self, money):
        self._remaining = money
        self._change = {}

    def get_remaining(self):
        return self._remaining

    def set_remaining(self, remaining):
        self._remaining = remaining

    def get_change(self):
        return self._change

    def add_change(self, change):
        self._change.update(change)


class Handler(metaclass=abc.ABCMeta):
    def __init__(self):
        self._next = None

    @abc.abstractmethod
    def set_next(self, handler):
        pass

    @abc.abstractmethod
    def handle(self, request):
        pass


class ATMDispenserHandler(Handler):
    def set_next(self, handler):
        self._next = handler
        return handler

    @abc.abstractmethod
    def handle(self, request):
        if self._next:
            return self._next.handle(request)

        return request


class DispenserHandler(ATMDispenserHandler):
    def __init__(self, change):
        super().__init__()
        self._change = change


    def handle(self, request):
        if request.get_remaining() < self._change:
            return super().handle(request)

        change = request.get_remaining() // self._change
        remaining = request.get_remaining() % self._change

        request.add_change({self._change: change})
        request.set_remaining(remaining)

        return super().handle(request)


class Dispenser:
    def dispense(self, money):
        chain1 = DispenserHandler(50)
        chain2 = DispenserHandler(20)
        chain3 = DispenserHandler(10)
        chain4 = DispenserHandler(5)

        chain1.set_next(chain2).set_next(chain3).set_next(chain4)

        return chain1.handle(Request(money))

