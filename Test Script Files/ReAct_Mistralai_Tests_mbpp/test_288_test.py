import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_modular_inverse_positive(self):
        self.assertEqual(modular_inverse([2, 3, 4, 5], 10, 7), 3)
        self.assertEqual(modular_inverse([1, 2, 3, 4], 10, 5), 3)
        self.assertEqual(modular_inverse([6, 7, 8, 9], 10, 7), 1)

    def test_modular_inverse_zero(self):
        self.assertRaises(ValueError, modular_inverse, [0], 10, 7)

    def test_modular_inverse_negative(self):
        self.assertRaises(ValueError, modular_inverse, [-1, -2, -3, -4], 10, 7)

    def test_modular_inverse_empty(self):
        self.assertRaises(ValueError, modular_inverse, [], 10, 7)

    def test_modular_inverse_single_element(self):
        self.assertEqual(modular_inverse([1], 10, 7), 1)

    def test_modular_inverse_large_input(self):
        self.assertEqual(modular_inverse([1000000000000000000, 1000000000000000001], 1000000000000000003, 7), 1)
