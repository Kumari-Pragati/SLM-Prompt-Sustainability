import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(modular_inverse([1, 2, 3], 4, 5), 3)
        self.assertEqual(modular_inverse([4, 5, 6], 7, 8), 6)

    def test_edge_cases(self):
        self.assertEqual(modular_inverse([0], 1, 2), 0)
        self.assertEqual(modular_inverse([1], 2, 3), 1)
        self.assertEqual(modular_inverse([2], 3, 4), 2)
        self.assertEqual(modular_inverse([3], 4, 5), 1)
        self.assertEqual(modular_inverse([4], 5, 6), 4)
        self.assertEqual(modular_inverse([5], 6, 7), 5)

    def test_boundary_conditions(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 6, 7), 5)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5, 6], 7, 8), 6)

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, modular_inverse, [], 1, 2)
        self.assertRaises(ValueError, modular_inverse, [1], 0, 2)
        self.assertRaises(ValueError, modular_inverse, [1], 2, 0)
