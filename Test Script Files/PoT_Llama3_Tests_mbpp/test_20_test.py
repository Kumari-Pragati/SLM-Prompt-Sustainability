import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_typical_case(self):
        self.assertFalse(is_woodall(0))
        self.assertTrue(is_woodall(1))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(3))
        self.assertTrue(is_woodall(4))
        self.assertFalse(is_woodall(5))

    def test_edge_case(self):
        self.assertFalse(is_woodall(10))
        self.assertFalse(is_woodall(20))
        self.assertFalse(is_woodall(30))
        self.assertFalse(is_woodall(40))
        self.assertFalse(is_woodall(50))

    def test_corner_case(self):
        self.assertFalse(is_woodall(100))
        self.assertFalse(is_woodall(200))
        self.assertFalse(is_woodall(300))
        self.assertFalse(is_woodall(400))
        self.assertFalse(is_woodall(500))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_woodall('a')
        with self.assertRaises(TypeError):
            is_woodall(None)
