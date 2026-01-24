import unittest
from mbpp_828_code import count_alpha_dig_spl

class TestCountAlphaDigSpl(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_alpha_dig_spl("Hello123!"), (5, 3, 1))

    def test_edge_case_empty_string(self):
        self.assertEqual(count_alpha_dig_spl(""), (0, 0, 0))

    def test_edge_case_single_char(self):
        self.assertEqual(count_alpha_dig_spl("a"), (1, 0, 0))
        self.assertEqual(count_alpha_dig_spl("1"), (0, 1, 0))
        self.assertEqual(count_alpha_dig_spl("!"), (0, 0, 1))

    def test_edge_case_all_alphabets(self):
        self.assertEqual(count_alpha_dig_spl("abcdefghijklmnopqrstuvwxyz"), 26, 0, 0)

    def test_edge_case_all_digits(self):
        self.assertEqual(count_alpha_dig_spl("0123456789"), 0, 10, 0)

    def test_edge_case_all_special_chars(self):
        self.assertEqual(count_alpha_dig_spl("!@#$%^&*()"), 0, 0, 10)

    def test_edge_case_mixed(self):
        self.assertEqual(count_alpha_dig_spl("Hello123!@#"), 5, 3, 4)

    def test_edge_case_non_ascii(self):
        self.assertEqual(count_alpha_dig_spl("Hello123!@#€"), 5, 3, 4)
