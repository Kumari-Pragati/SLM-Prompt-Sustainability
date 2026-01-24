import unittest
from mbpp_113_code import check_integer

class TestCheckInteger(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(check_integer("12345"))

    def test_simple_false(self):
        self.assertFalse(check_integer("abcde"))

    def test_edge_empty(self):
        self.assertIsNone(check_integer(""))

    def test_edge_single_digit(self):
        self.assertTrue(check_integer("1"))

    def test_edge_negative(self):
        self.assertTrue(check_integer("-12345"))

    def test_edge_positive(self):
        self.assertTrue(check_integer("+12345"))

    def test_edge_mixed(self):
        self.assertTrue(check_integer("-12345abc"))

    def test_edge_invalid(self):
        self.assertFalse(check_integer("123abc"))

    def test_edge_invalid_start(self):
        self.assertFalse(check_integer("abc123"))

    def test_edge_invalid_end(self):
        self.assertFalse(check_integer("123abc"))
