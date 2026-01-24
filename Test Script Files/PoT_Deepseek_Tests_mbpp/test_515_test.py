import unittest
from mbpp_515_code import modular_sum

class TestModularSum(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(modular_sum([1, 2, 3], 3, 10))
        self.assertFalse(modular_sum([1, 2, 3], 3, 6))

    def test_edge_case(self):
        self.assertFalse(modular_sum([], 0, 10))
        self.assertFalse(modular_sum([1], 1, 1))

    def test_boundary_case(self):
        self.assertTrue(modular_sum([0, 0, 0], 3, 10))
        self.assertFalse(modular_sum([1, 2, 3], 3, 0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            modular_sum("1, 2, 3", 3, 10)
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], "3", 10)
        with self.assertRaises(TypeError):
            modular_sum([1, 2, 3], 3, "10")
