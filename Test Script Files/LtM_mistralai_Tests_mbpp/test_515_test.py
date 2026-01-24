import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(modular_sum([1], 1, 1))
        self.assertTrue(modular_sum([1, 2], 2, 3))
        self.assertFalse(modular_sum([1, 2], 3, 3))
        self.assertTrue(modular_sum([1, 2, 3], 3, 4))
        self.assertFalse(modular_sum([1, 2, 3], 4, 4))

    def test_edge_cases(self):
        self.assertTrue(modular_sum([], 0, 1))
        self.assertFalse(modular_sum([], 1, 1))
        self.assertTrue(modular_sum([1], 0, 1))
        self.assertFalse(modular_sum([1], 1, 0))
        self.assertTrue(modular_sum([1, 2], 0, 1))
        self.assertFalse(modular_sum([1, 2], 1, 0))

    def test_boundary_conditions(self):
        self.assertTrue(modular_sum([1, 2, 3, 4], 4, 5))
        self.assertFalse(modular_sum([1, 2, 3, 4], 5, 5))
        self.assertTrue(modular_sum([1, 2, 3, 4], 5, 6))
        self.assertFalse(modular_sum([1, 2, 3, 4], 6, 6))

    def test_complex_cases(self):
        self.assertTrue(modular_sum([1, 2, 3, 4, 5], 5, 6))
        self.assertFalse(modular_sum([1, 2, 3, 4, 5], 6, 6))
        self.assertTrue(modular_sum([1, 2, 3, 4, 5], 6, 7))
        self.assertFalse(modular_sum([1, 2, 3, 4, 5], 7, 7))
        self.assertTrue(modular_sum([1, 2, 3, 4, 5], 7, 8))
        self.assertFalse(modular_sum([1, 2, 3, 4, 5], 8, 8))
