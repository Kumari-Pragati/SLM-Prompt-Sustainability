import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_normal_input(self):
        self.assertTrue(is_upper("HELLO"))

    def test_edge_case_uppercase(self):
        self.assertTrue(is_upper("A"))
        self.assertTrue(is_upper("Z"))

    def test_edge_case_lowercase(self):
        self.assertFalse(is_upper("a"))
        self.assertFalse(is_upper("z"))

    def test_edge_case_empty_string(self):
        self.assertTrue(is_upper(""))

    def test_edge_case_whitespace(self):
        self.assertTrue(is_upper("\t"))
        self.assertTrue(is_upper(" "))
        self.assertTrue(is_upper("\n"))

    def test_invalid_input_non_string(self):
        self.assertRaises(TypeError, is_upper, 123)
        self.assertRaises(TypeError, is_upper, [])
        self.assertRaises(TypeError, is_upper, (1, 2, 3))
        self.assertRaises(TypeError, is_upper, None)
