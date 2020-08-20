from behavioral.chain_responsibility import ATMDispenser


class TestDispenser:
    def test_it_despense_change_of_50(self):
        dispenser = ATMDispenser()
        assert dispenser.dispense(100).get_change()[50] == 2

    def test_it_despense_change_of_20(self):
        dispenser = ATMDispenser()
        assert dispenser.dispense(40).get_change()[20] == 2

    def test_it_despense_change_of_10(self):
        dispenser = ATMDispenser()
        assert dispenser.dispense(15).get_change()[10] == 1

    def test_it_despense_change_of_5(self):
        dispenser = ATMDispenser()
        assert dispenser.dispense(15).get_change()[5] == 1

    def test_it_remains_money_after_dispense(self):
        dispenser = ATMDispenser()
        dispensed = dispenser.dispense(17)

        assert dispensed.get_change()[10] == 1
        assert dispensed.get_change()[5] == 1
        assert dispensed.get_remaining() == 2
