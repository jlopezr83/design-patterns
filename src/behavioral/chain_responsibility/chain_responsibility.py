from abc import ABCMeta


class Handler(metaclass=ABCMeta):
    """
    Defines an interface for handling requests
    """
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    def handle(self, request):
        if self._next:
            return self._next.handle(request)

        return request


class DispenserHandler(Handler):
    """
    Handles requests it is responsible for, if it can't handle the request, it forwards the request to its successor
    """
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


class ATMDispenser:
    """
    Client. It initiates the request to a DispenserHandler on the chain
    """
    def dispense(self, money_request):
        chain1 = DispenserHandler(50)
        chain2 = DispenserHandler(20)
        chain3 = DispenserHandler(10)
        chain4 = DispenserHandler(5)

        chain1.set_next(chain2).set_next(chain3).set_next(chain4)

        return chain1.handle(MoneyRequest(money_request))


class MoneyRequest:
    """
    Request. Class to store the status of the request
    """
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
