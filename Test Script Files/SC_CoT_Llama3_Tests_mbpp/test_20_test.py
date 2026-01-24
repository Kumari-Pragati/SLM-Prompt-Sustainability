import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertFalse(is_woodall(0))
        self.assertTrue(is_woodall(1))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(4))
        self.assertTrue(is_woodall(5))

    def test_edge_and_boundary_cases(self):
        self.assertFalse(is_woodall(3))
        self.assertFalse(is_woodall(6))
        self.assertFalse(is_woodall(8))
        self.assertTrue(is_woodall(9))
        self.assertFalse(is_woodall(10))

    def test_special_and_corner_cases(self):
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(6))
        self.assertFalse(is_woodall(8))
        self.assertTrue(is_woodall(9))
        self.assertFalse(is_woodall(10))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_woodall('a')
