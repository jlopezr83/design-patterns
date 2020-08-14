from abc import ABCMeta
import re


REG_EXP_LOWERCASE_CHAR = '[a-z]'
REG_EXP_UPPERCASE_CHAR = '[A-Z]'
REG_EXP_NUMBER = '[0-9]'


class RegExp(metaclass=ABCMeta):
    def __init__(self):
        self._reg_exp = None

    def get_reg_exp(self):
        """
        Returns the regular expression of the pattern
        :return: string: Regular expression
        """
        return f'({self._reg_exp})'

    def match(self, input_string):
        """
        Return True in case the input_string match with the reg_exp or False in case it doesn't match
        :param input_string: input_string to check if it match with the reg_exp
        :return: bool: True if it's a valid pattern and False if it isn't
        """
        try:
            matcher = re.compile(self.get_reg_exp())
            match = matcher.match(input_string)
        except Exception:
            raise ValueError('It needs a valid regular expression and a valid input string')

        if not match or match.group() != input_string:  # No match or the input string is not exactly equal
            return False
        return True


class CompositeRegExp(RegExp):
    def __init__(self):
        super().__init__()
        self._reg_exps = []

    def get_reg_exp(self):
        """
        Calculate the regular expression based on its elements
        :return: string: Composite regular expression
        """
        composed_exp = ''
        for reg_exp in self._reg_exps:
            composed_exp += f'({reg_exp.get_reg_exp()})'

        return composed_exp

    def add(self, reg_exp):
        """
        Append new AbstractPattern elements
        and recalculate the reg exp to keep the consistence
        :param pattern:
        :return:
        """
        self._reg_exps.append(reg_exp)


class RegExpLowerCase(RegExp):
    def __init__(self):
        super().__init__()
        self._reg_exp = REG_EXP_LOWERCASE_CHAR


class RegExpUpperCase(RegExp):
    def __init__(self):
        super().__init__()
        self._reg_exp = REG_EXP_UPPERCASE_CHAR


class RegExpNumber(RegExp):
    def __init__(self):
        super().__init__()
        self._reg_exp = REG_EXP_NUMBER