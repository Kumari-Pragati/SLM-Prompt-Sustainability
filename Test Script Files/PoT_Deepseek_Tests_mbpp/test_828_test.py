import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_alpha_dig_spl("abc123"), (3, 3, 0))

    def test_edge_case_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_boundary_case_only_alphabets(self):
        self.assertEqual(count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz"), (26, 0, 0))

    def test_boundary_case_only_digits(self):
        self.assertEqual(count_alpha_dig_spl("0123456789"), (0, 10, 0))

    def test_corner_case_special_characters(self):
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), (0, 0, 10))

    def test_corner_case_mixed_characters(self):
        self.assertEqual(count_alpha_dig_spl("abc123!@#"), (3, 3, 3))
