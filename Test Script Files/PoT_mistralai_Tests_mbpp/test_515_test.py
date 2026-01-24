import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertFalse(modular_sum([1, 2, 3], 5, 7))
        self.assertTrue(modular_sum([1, 2, 4], 6, 7))
        self.assertFalse(modular_sum([1, 2, 3], 7, 7))
        self.assertTrue(modular_sum([1, 2, 4], 8, 7))

    def test_edge_cases(self):
        self.assertFalse(modular_sum([], 0, 1))
        self.assertFalse(modular_sum([1], 1, 1))
        self.assertTrue(modular_sum([1], 2, 1))
        self.assertFalse(modular_sum([1, 2], 1, 1))
        self.assertTrue(modular_sum([1, 2], 2, 1))
        self.assertTrue(modular_sum([1, 2], 3, 1))
        self.assertFalse(modular_sum([1, 2, 3], 0, 1))
        self.assertTrue(modular_sum([1, 2, 3], 4, 1))
        self.assertTrue(modular_sum([1, 2, 3], 5, 2))
        self.assertFalse(modular_sum([1, 2, 3], 6, 2))
        self.assertTrue(modular_sum([1, 2, 3], 7, 2))
        self.assertFalse(modular_sum([1, 2, 3], 8, 2))
