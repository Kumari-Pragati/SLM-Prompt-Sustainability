import unittest
from mbpp_20_code import is_woodall

class TestIsWoodall(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_woodall(1))
        self.assertTrue(is_woodall(15))
        self.assertTrue(is_woodall(127))
        self.assertTrue(is_woodall(4095))

    def test_edge_cases(self):
        self.assertFalse(is_woodall(0))
        self.assertFalse(is_woodall(2))
        self.assertFalse(is_woodall(3))
        self.assertFalse(is_woodall(4))
        self.assertFalse(is_woodall(8))
        self.assertFalse(is_woodall(16))
        self.assertFalse(is_woodall(65536))

    def test_corner_cases(self):
        self.assertTrue(is_woodall(65535))
        self.assertFalse(is_woodall(65536))
        self.assertFalse(is_woodall(131072))
        self.assertFalse(is_woodall(262144))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_woodall('1')
        with self.assertRaises(TypeError):
            is_woodall(None)
        with self.assertRaises(TypeError):
            is_woodall([])
        with self.assertRaises(TypeError):
            is_woodall({})
