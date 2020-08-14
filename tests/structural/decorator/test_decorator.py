from structural.decorator import round_decimals


class TestRoundDecimals:
    def test_it_round_number_decimals_by_default(self):
        @round_decimals
        def dummy_return_value(value):
            return value

        assert dummy_return_value(1.123456789) == 1.123

    def test_it_round_number_decimals_passed_as_argument(self):
        @round_decimals(num_decimals=2)
        def dummy_return_value(value):
            return value

        assert dummy_return_value(1.123456789) == 1.12
