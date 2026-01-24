import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):
    def test_typical_string(self):
        self.assertEqual(count_alpha_dig_spl("abc123"), (3, 3, 0))

    def test_string_with_special_chars(self):
        self.assertEqual(count_alpha_dig_spl("abc123!@#"), (3, 3, 3))

    def test_string_with_only_alphabets(self):
        self.assertEqual(count_alpha_dig_spl("abc"), (3, 0, 0))

    def test_string_with_only_digits(self):
        self.assertEqual(count_alpha_dig_spl("123"), (0, 3, 0))

    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_string_with_mixed_case(self):
        self.assertEqual(count_alpha_dig_spl("Abc123"), (3, 3, 0))

    def test_string_with_spaces(self):
        self.assertEqual(count_alpha_dig_spl("abc 123"), (3, 3, 1))
