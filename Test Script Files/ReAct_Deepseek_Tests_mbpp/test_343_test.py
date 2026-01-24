import unittest
from mbpp_343_code import dig_let

class TestDigLet(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(dig_let("a1b2c3"), (3, 3))

    def test_empty_string(self):
        self.assertEqual(dig_let(""), (0, 0))

    def test_all_digits(self):
        self.assertEqual(dig_let("123456"), (0, 6))

    def test_all_letters(self):
        self.assertEqual(dig_let("abcdef"), (6, 0))

    def test_mixed_case(self):
        self.assertEqual(dig_let("a1b2c3d4e5f6"), (6, 6))

    def test_mixed_case_with_special_chars(self):
        self.assertEqual(dig_let("a1b2c3!@#d4e5f6"), (6, 6))
