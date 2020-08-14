from structural.composite import CompositeRegExp, RegExpLowerCase, RegExpUpperCase, RegExpNumber


class TestComposite:
    def test_it_creates_composite_reg_exp(self):
        reg_exp_composite = CompositeRegExp()
        reg_exp_composite.add(RegExpLowerCase())
        reg_exp_composite.add(RegExpUpperCase())
        reg_exp_composite.add(RegExpNumber())

        assert reg_exp_composite.match('aA1') is True
        assert reg_exp_composite.match('1Aa') is False
