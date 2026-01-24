import unittest
from mbpp_887_code import is_odd

class TestIsOdd(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(6))

    def test_boundary_conditions(self):
        self.assertTrue(is_odd(0))
        self.assertFalse(is_odd(-1))
        self.assertFalse(is_odd(-2))

    def test_edge_cases(self):
        self.assertTrue(is_odd(10000000000000000000001))
        self.assertFalse(is_odd(10000000000000000000000))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_odd('a')
        with self.assertRaises(TypeError):
            is_odd(None)
        with self.assertRaises(TypeError):
            is_odd([1, 2, 3])
