import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(number_ctr("123abc"), 3)

    def test_edge_case_empty_string(self):
        self.assertEqual(number_ctr(""), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(number_ctr("1"), 1)

    def test_edge_case_single_non_digit(self):
        self.assertEqual(number_ctr("a"), 0)

    def test_edge_case_all_digits(self):
        self.assertEqual(number_ctr("123456"), 6)

    def test_edge_case_all_non_digits(self):
        self.assertEqual(number_ctr("abc"), 0)

    def test_edge_case_mixed(self):
        self.assertEqual(number_ctr("123abc456"), 6)

    def test_edge_case_mixed_with_spaces(self):
        self.assertEqual(number_ctr("123 abc 456"), 6)

    def test_edge_case_mixed_with_punctuation(self):
        self.assertEqual(number_ctr("123!abc456"), 6)
