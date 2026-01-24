import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(15))
        self.assertTrue(is_woodall(127))
        self.assertTrue(is_woodall(4095))

    def test_edge_and_boundary_conditions(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(-1))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(3))
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(8))

    def test_corner_cases(self):
        self.assertTrue(is_woodall(1023))
        self.assertFalse(is_woodall(1024))
        self.assertFalse(is_woodall(2047))
        self.assertFalse(is_woodall(2048))
