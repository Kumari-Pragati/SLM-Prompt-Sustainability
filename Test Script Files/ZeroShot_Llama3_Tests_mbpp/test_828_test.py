import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_string_with_alphabets(self):
        self.assertEqual(count_alpha_dig_spl("Hello"), (5, 0, 0))

    def test_string_with_digits(self):
        self.assertEqual(count_alpha_dig_spl("123456"), (0, 6, 0))

    def test_string_with_special_characters(self):
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), (0, 0, 7))

    def test_string_with_mixed_characters(self):
        self.assertEqual(count_alpha_dig_spl("Hello123!@#"), (5, 3, 3))

    def test_string_with_spaces(self):
        self.assertEqual(count_alpha_dig_spl("Hello World"), (11, 0, 2))
