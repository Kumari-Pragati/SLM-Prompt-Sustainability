import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertFalse(modular_sum([1, 2, 3], 3, 4))
        self.assertTrue(modular_sum([1, 2, 3], 4, 4))
        self.assertFalse(modular_sum([1, 2, 3], 5, 4))
        self.assertTrue(modular_sum([1, 2, 3], 6, 4))

    def test_edge_case(self):
        self.assertFalse(modular_sum([], 0, 1))
        self.assertTrue(modular_sum([0], 1, 1))
        self.assertFalse(modular_sum([0], 2, 1))
        self.assertTrue(modular_sum([0], 1, 0))
        self.assertFalse(modular_sum([1], 0, 1))
        self.assertTrue(modular_sum([1], 1, 1))
        self.assertFalse(modular_sum([1], 2, 1))
        self.assertTrue(modular_sum([1], 1, 0))

    def test_invalid_input(self):
        self.assertRaises(TypeError, modular_sum, [1, 2, 3], 'n', 4)
        self.assertRaises(TypeError, modular_sum, [1, 2, 3], 4, 'm')
        self.assertRaises(TypeError, modular_sum, [1, 2, 3], 4, [m])
        self.assertRaises(ValueError, modular_sum, [1, 2, 3], -1, 4)
        self.assertRaises(ValueError, modular_sum, [1, 2, 3], 4, -1)
