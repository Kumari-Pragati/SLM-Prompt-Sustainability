import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_alpha_dig_spl("abc123"), (3, 3, 0))

    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_all_special_characters(self):
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), (0, 0, 10))

    def test_all_digits(self):
        self.assertEqual(count_alpha_dig_spl("1234567890"), (0, 10, 0))

    def test_all_alphabets(self):
        self.assertEqual(count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz"), (26, 0, 0))

    def test_mixed_case(self):
        self.assertEqual(count_alpha_dig_spl("abc123!@#"), (3, 3, 3))

    def test_mixed_case_with_uppercase(self):
        self.assertEqual(count_alpha_dig_spl("Abc123!@#"), (3, 3, 3))

    def test_special_characters_only(self):
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), (0, 0, 10))

    def test_digits_only(self):
        self.assertEqual(count_alpha_dig_spl("1234567890"), (0, 10, 0))

    def test_alphabets_only(self):
        self.assertEqual(count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz"), (26, 0, 0))
