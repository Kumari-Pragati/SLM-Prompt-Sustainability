import unittest
from mbpp_913_code import end_num

class TestEndNum(unittest.TestCase):
    def test_simple_true(self):
        self.assertTrue(end_num("hello123"))

    def test_simple_false(self):
        self.assertFalse(end_num("hello"))

    def test_edge_empty_string(self):
        self.assertFalse(end_num(""))

    def test_edge_single_digit(self):
        self.assertTrue(end_num("123"))

    def test_edge_multiple_digits(self):
        self.assertTrue(end_num("hello456"))

    def test_edge_non_digit(self):
        self.assertFalse(end_num("helloabc"))

    def test_edge_mixed_digits(self):
        self.assertTrue(end_num("hello123abc"))
