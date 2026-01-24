import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):
    def test_modular_inverse_typical(self):
        self.assertEqual(modular_inverse([2, 3, 4, 5], 10, 7), 3)
        self.assertEqual(modular_inverse([1, 2, 3, 4], 10, 5), 4)
        self.assertEqual(modular_inverse([6, 7, 8, 9], 10, 13), 9)

    def test_modular_inverse_edge(self):
        self.assertEqual(modular_inverse([0, 1, 2, 3], 10, 7), 3)
        self.assertEqual(modular_inverse([4, 5, 6, 7], 10, 7), None)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 10, 7), 3)

    def test_modular_inverse_invalid(self):
        self.assertRaises(ValueError, modular_inverse, [], 10, 7)
        self.assertRaises(ValueError, modular_inverse, [1], 0, 7)
        self.assertRaises(ValueError, modular_inverse, [1, 2], 10, 0)
