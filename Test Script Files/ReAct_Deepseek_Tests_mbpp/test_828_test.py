import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_alpha_dig_spl("a1b2c3"), (3, 2, 1))

    def test_all_alphabets(self):
        self.assertEqual(count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz"), (26, 0, 0))

    def test_all_digits(self):
        self.assertEqual(count_alpha_dig_spl("0123456789"), (0, 10, 0))

    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_special_characters(self):
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), (0, 0, 10))

    def test_mixed_case(self):
        self.assertEqual(count_alpha_dig_spl("a1@b2#c3$"), (3, 2, 2))

    def test_mixed_string(self):
        self.assertEqual(count_alpha_dig_spl("a1b2@c3$4"), (3, 2, 2))

    def test_whitespace(self):
        self.assertEqual(count_alpha_dig_spl("a1 b2 c3"), (3, 2, 1))
