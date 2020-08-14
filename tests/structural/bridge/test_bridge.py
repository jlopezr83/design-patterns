from structural.bridge import StringFormatter, FormatterLowerCase, FormatterUpperCase


class TestBridge:
    def test_it_formats_string_to_lowercase(self):
        lowercase_formatter = FormatterLowerCase()
        formatter = StringFormatter(lowercase_formatter)

        assert formatter.format('ABC') == 'abc'

    def test_it_formats_string_to_uppercase(self):
        uppercase_formatter = FormatterUpperCase()
        formatter = StringFormatter(uppercase_formatter)

        assert formatter.format('abc') == 'ABC'
