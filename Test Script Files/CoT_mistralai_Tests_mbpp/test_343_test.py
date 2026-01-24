import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(dig_let(''), (0, 0))

    def test_all_digits(self):
        self.assertEqual(dig_let('12345'), (0, 5))

    def test_all_letters(self):
        self.assertEqual(dig_let('abcdefg'), (7, 0))

    def test_mixed_case(self):
        self.assertEqual(dig_let('A1B2C3'), (3, 3))

    def test_special_characters(self):
        self.assertEqual(dig_let('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), (0, 0))

    def test_single_digit(self):
        self.assertEqual(dig_let('5'), (0, 1))

    def test_single_letter(self):
        self.assertEqual(dig_let('a'), (1, 0))

    def test_long_string(self):
        self.assertEqual(dig_let('0123456789abcdefghijklmnopqrstuvwxyz'), (26, 10))
