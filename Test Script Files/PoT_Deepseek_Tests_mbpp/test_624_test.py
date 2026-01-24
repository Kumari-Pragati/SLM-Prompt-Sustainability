import unittest
from mbpp_624_code import is_upper

class TestIsUpper(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_upper("abc"))
        self.assertFalse(is_upper("ABC"))

    def test_edge_cases(self):
        self.assertTrue(is_upper(""))
        self.assertFalse(is_upper(""))

    def test_corner_cases(self):
        self.assertTrue(is_upper("123"))
        self.assertFalse(is_upper("!@#"))
