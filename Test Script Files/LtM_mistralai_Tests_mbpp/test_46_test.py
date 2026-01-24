import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):
    def test_simple_distinct(self):
        self.assertTrue(test_distinct([1, 2, 3]))
        self.assertTrue(test_distinct([4, 5, 6]))
        self.assertTrue(test_distinct([7, 8, 9]))

    def test_edge_cases(self):
        self.assertTrue(test_distinct([]))
        self.assertTrue(test_distinct([1]))
        self.assertTrue(test_distinct([1, 1]))
        self.assertTrue(test_distinct([1, 2, 2]))
        self.assertTrue(test_distinct([1, 2, 3, 3]))

    def test_complex_distinct(self):
        self.assertTrue(test_distinct([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        self.assertFalse(test_distinct([1, 1, 2, 2, 3, 3]))
        self.assertFalse(test_distinct([1, 1, 1, 2, 3, 3]))
        self.assertFalse(test_distinct([1, 1, 1, 1, 2, 3, 3]))
        self.assertFalse(test_distinct([1, 1, 1, 1, 1, 2, 3, 3]))
