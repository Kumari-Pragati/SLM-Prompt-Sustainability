import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(dig_let(''), (0, 0))

    def test_only_digits(self):
        self.assertEqual(dig_let('12345'), (0, 5))

    def test_only_letters(self):
        self.assertEqual(dig_let('abcdefg'), (7, 0))

    def test_mixed_case(self):
        self.assertEqual(dig_let('AbCd123EfG456'), (8, 4))

    def test_leading_digit(self):
        self.assertEqual(dig_let('1abc'), (3, 1))

    def test_trailing_digit(self):
        self.assertEqual(dig_let('abc1'), (3, 1))

    def test_leading_and_trailing_digits(self):
        self.assertEqual(dig_let('1abc2'), (3, 2))

    def test_special_characters(self):
        self.assertEqual(dig_let('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), (0, 0))

    def test_long_string(self):
        long_string = 'a' * 100 + '1' * 100
        self.assertEqual(dig_let(long_string), (100, 100))
