import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_alpha_dig_spl("Hello123!"), (5, 3, 1))

    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_all_alphabets(self):
        self.assertEqual(count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz"), 26, 0, 0)

    def test_all_digits(self):
        self.assertEqual(count_alpha_dig_spl("0123456789"), 0, 10, 0)

    def test_all_special_chars(self):
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), 0, 0, 10)

    def test_mixed_input(self):
        self.assertEqual(count_alpha_dig_spl("Hello123!@#"), 5, 3, 3)

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            count_alpha_dig_spl(123)
