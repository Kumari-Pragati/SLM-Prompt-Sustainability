import unittest
from mbpp_46_code import test_distinct

class TestDistinct(unittest.TestCase):
    def test_typical(self):
        self.assertTrue(test_distinct([1, 2, 3, 4]))
        self.assertTrue(test_distinct([5, 5, 6, 7]))
        self.assertTrue(test_distinct([1.0, 2.0, 3.0]))

    def test_edge(self):
        self.assertTrue(test_distinct([]))
        self.assertTrue(test_distinct([1]))
        self.assertTrue(test_distinct([1, 1]))

    def test_corner(self):
        self.assertFalse(test_distinct([1, 1, 1, 2]))
        self.assertFalse(test_distinct([1, 1, 1, 1.0]))
        self.assertFalse(test_distinct([None, None, None]))
        self.assertFalse(test_distinct([True, False, True]))
