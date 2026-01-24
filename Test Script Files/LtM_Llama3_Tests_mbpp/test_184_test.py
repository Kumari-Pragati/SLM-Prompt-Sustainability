import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificnum(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(greater_specificnum([1, 2, 3, 4, 5], 3))
        self.assertFalse(greater_specificnum([1, 2, 3, 4, 5], 6))

    def test_empty_list(self):
        self.assertFalse(greater_specificnum([], 1))

    def test_single_element_list(self):
        self.assertTrue(greater_specificnum([5], 5))
        self.assertFalse(greater_specificnum([5], 4))

    def test_edge_cases(self):
        self.assertTrue(greater_specificnum([1, 1, 1, 1, 1], 1))
        self.assertFalse(greater_specificnum([1, 1, 1, 1, 1], 2))

    def test_max_value(self):
        self.assertTrue(greater_specificnum([5, 5, 5, 5, 5], 5))

    def test_min_value(self):
        self.assertFalse(greater_specificnum([1, 1, 1, 1, 1], 0))
