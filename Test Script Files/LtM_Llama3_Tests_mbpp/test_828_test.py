import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_alpha_string(self):
        self.assertEqual(count_alpha_dig_spl("abcdef"), (6, 0, 0))

    def test_digit_string(self):
        self.assertEqual(count_alpha_dig_spl("123456"), (0, 6, 0))

    def test_alpha_digit_string(self):
        self.assertEqual(count_alpha_dig_spl("abc123"), (3, 3, 0))

    def test_alpha_digit_special_string(self):
        self.assertEqual(count_alpha_dig_spl("abc123!"), (3, 3, 1))

    def test_edge_case_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_edge_case_single_char(self):
        self.assertEqual(count_alpha_dig_spl("a"), (1, 0, 0))

    def test_edge_case_single_digit(self):
        self.assertEqual(count_alpha_dig_spl("1"), (0, 1, 0))

    def test_edge_case_single_special_char(self):
        self.assertEqual(count_alpha_dig_spl("!"), (0, 0, 1))

    def test_edge_case_all_alpha(self):
        self.assertEqual(count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz"), (26, 0, 0))

    def test_edge_case_all_digit(self):
        self.assertEqual(count_alpha_dig_spl("0123456789"), (0, 10, 0))

    def test_edge_case_all_special(self):
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), (0, 0, 10))
