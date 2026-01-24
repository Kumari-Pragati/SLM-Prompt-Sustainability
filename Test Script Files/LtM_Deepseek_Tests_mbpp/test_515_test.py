import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 10))
        self.assertFalse(modular_sum([1, 2, 3], 3, 6))

    def test_edge_conditions(self):
        self.assertFalse(modular_sum([], 0, 10))
        self.assertFalse(modular_sum([1], 1, 1))
        self.assertTrue(modular_sum([0], 1, 10))

    def test_boundary_conditions(self):
        self.assertTrue(modular_sum([10, 20, 30], 3, 100))
        self.assertFalse(modular_sum([99, 1, 2], 3, 100))

    def test_complex_cases(self):
        self.assertTrue(modular_sum([1, 2, 3, 4, 5], 5, 10))
        self.assertFalse(modular_sum([1, 2, 3, 4, 5], 5, 6))
