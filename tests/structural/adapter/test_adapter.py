from structural.adapter import AmericanPlug, AmericanToEuropeanPlug, Boiler


class TestAdapter:
    def test_it_adapt_american_to_european_plugs(self):
        american_plug = AmericanPlug()
        adapter = AmericanToEuropeanPlug(american_plug)
        boiler = Boiler(adapter)

        assert boiler.boil() is True

    def test_it_not_boil_with_american_plug(self):
        american_plug = AmericanPlug()
        boiler = Boiler(american_plug)

        assert boiler.boil() is False
