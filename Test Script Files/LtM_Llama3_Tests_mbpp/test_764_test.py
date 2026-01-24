import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(number_ctr(""), 0)

    def test_single_digit(self):
        self.assertEqual(number_ctr("1"), 1)

    def test_multiple_digits(self):
        self.assertEqual(number_ctr("123"), 3)

    def test_non_numeric_characters(self):
        self.assertEqual(number_ctr("abc123"), 3)

    def test_mixed_characters(self):
        self.assertEqual(number_ctr("abc123def"), 3)

    def test_all_digits(self):
        self.assertEqual(number_ctr("1234567890"), 10)

    def test_all_non_digits(self):
        self.assertEqual(number_ctr("abcdef"), 0)

    def test_edge_case(self):
        self.assertEqual(number_ctr("0123456789"), 10)
