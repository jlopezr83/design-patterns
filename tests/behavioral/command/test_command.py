from behavioral.command import TurnOnCommand, TurnOffCommand, ComplexCommand, Receiver, Invoker, Computer


class TestCommand:
    def test_it_creates_command(self):
        computer = Computer()
        turn_on_command = TurnOnCommand(computer)
        turn_off_command = TurnOffCommand(computer)
        turn_invoker = Invoker()

        turn_invoker.register('on', turn_on_command)
        turn_invoker.register('off', turn_off_command)

        turn_invoker.execute('on')
        assert computer.get_power() is True

        turn_invoker.execute('off')
        assert computer.get_power() is False

    def test_it_creates_complex_command(self):
        computer = Computer()
        receiver = Receiver()
        complex_command = ComplexCommand(receiver, computer)
        invoker = Invoker()

        invoker.register('complex', complex_command)
        invoker.execute('complex')
        assert computer.get_counter() == 2


