import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(modular_inverse([2, 3, 4, 5], 10, 7), 3)
        self.assertEqual(modular_inverse([1, 2, 3, 4], 10, 5), 4)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(modular_inverse([0, 1, 2, 3], 4, 5), 3)
        self.assertEqual(modular_inverse([10, 11, 12, 13], 14, 5), 0)
        self.assertEqual(modular_inverse([1, 2, 3, 4], 1, 5), 0)
        self.assertEqual(modular_inverse([1, 2, 3, 4], 2, 5), 0)

    def test_special_cases(self):
        self.assertEqual(modular_inverse([1], 1, 1), 1)
        self.assertEqual(modular_inverse([1], 2, 1), 0)
        self.assertEqual(modular_inverse([1, 2], 2, 1), 0)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, modular_inverse, [1, 2, 3], 0, 5)
        self.assertRaises(ValueError, modular_inverse, [1, 2, 3], 10, 0)
        self.assertRaises(ValueError, modular_inverse, [1, 2, 3], 10, 11)
