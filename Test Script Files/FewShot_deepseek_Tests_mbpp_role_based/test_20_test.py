import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(15))
        self.assertTrue(is_woodall(442361))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(3))
        self.assertFalse(is_woodall(4))

    def test_edge_cases(self):
        self.assertTrue(is_woodall(1))
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(-1))

    def test_boundary_conditions(self):
        self.assertTrue(is_woodall(2**65535 - 1))
        self.assertFalse(is_woodall(2**65535))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_woodall('1')
        with self.assertRaises(TypeError):
            is_woodall(None)
