import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 5))
        self.assertTrue(modular_sum([4, 5, 6], 6, 10))
        self.assertTrue(modular_sum([7, 8, 9], 9, 11))

    def test_edge_and_boundary(self):
        self.assertTrue(modular_sum([0], 0, 1))
        self.assertTrue(modular_sum([1], 1, 1))
        self.assertTrue(modular_sum([1, 2], 2, 3))
        self.assertTrue(modular_sum([1, 2, 3], 3, 3))
        self.assertTrue(modular_sum([1, 2, 3], 4, 3))
        self.assertTrue(modular_sum([1, 2, 3], 5, 3))
        self.assertFalse(modular_sum([1, 2, 3], 6, 3))
        self.assertFalse(modular_sum([1, 2, 3], 7, 3))

        self.assertFalse(modular_sum([], 0, 1))
        self.assertFalse(modular_sum([1], 0, 1))
        self.assertFalse(modular_sum([1, 2], 0, 1))
        self.assertFalse(modular_sum([1, 2, 3], 0, 1))

        self.assertTrue(modular_sum([1, 2, 3], 3, 0))
        self.assertTrue(modular_sum([1, 2, 3], 3, -1))
        self.assertFalse(modular_sum([1, 2, 3], 0, -1))
        self.assertFalse(modular_sum([1, 2, 3], -1, -1))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, modular_sum, [1, 2, 3], 'n', 5)
        self.assertRaises(TypeError, modular_sum, [1, 2, 3], 5, 'm')
        self.assertRaises(TypeError, modular_sum, [1, 2, 3], 5, [m])
