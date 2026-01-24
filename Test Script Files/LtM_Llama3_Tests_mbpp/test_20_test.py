import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(is_woodall(1))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(6))
        self.assertFalse(is_woodall(8))

    def test_edge(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(3))
        self.assertFalse(is_woodall(5))
        self.assertFalse(is_woodall(7))
        self.assertFalse(is_woodall(9))

    def test_complex(self):
        self.assertTrue(is_woodall(11))
        self.assertTrue(is_woodall(13))
        self.assertTrue(is_woodall(17))
        self.assertTrue(is_woodall(19))
        self.assertFalse(is_woodall(10))
