import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_woodall(3))
        self.assertTrue(is_woodall(5))
        self.assertTrue(is_woodall(7))
        self.assertTrue(is_woodall(9))
        self.assertFalse(is_woodall(10))
        self.assertFalse(is_woodall(12))

    def test_edge_cases(self):
        self.assertTrue(is_woodall(1))
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(-1))
