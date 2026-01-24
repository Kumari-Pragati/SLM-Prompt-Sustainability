import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):
    def test_typical_true(self):
        self.assertTrue(check_integer("12345"))

    def test_typical_false(self):
        self.assertFalse(check_integer("abcde"))

    def test_edge_positive(self):
        self.assertTrue(check_integer("+12345"))

    def test_edge_negative(self):
        self.assertTrue(check_integer("-12345"))

    def test_edge_zero(self):
        self.assertTrue(check_integer("0"))

    def test_edge_empty(self):
        self.assertIsNone(check_integer(""))

    def test_edge_single_digit(self):
        self.assertTrue(check_integer("1"))

    def test_edge_single_digit_negative(self):
        self.assertTrue(check_integer("-1"))

    def test_edge_single_digit_zero(self):
        self.assertTrue(check_integer("0"))

    def test_edge_single_digit_non_digit(self):
        self.assertFalse(check_integer("a"))

    def test_edge_multiple_digits_non_digit(self):
        self.assertFalse(check_integer("123a"))

    def test_edge_multiple_digits_non_digit_at_start(self):
        self.assertFalse(check_integer("a123"))

    def test_edge_multiple_digits_non_digit_at_end(self):
        self.assertFalse(check_integer("123a"))

    def test_edge_multiple_digits_non_digit_at_start_and_end(self):
        self.assertFalse(check_integer("a123a"))
