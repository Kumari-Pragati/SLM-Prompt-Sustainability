import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 5, 7), 3)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 6, 7), 5)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 7, 7), 1)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 8, 7), None)

    def test_negative_numbers(self):
        self.assertEqual(modular_inverse([-1, -2, -3, -4, -5], 5, 7), 4)
        self.assertEqual(modular_inverse([-1, -2, -3, -4, -5], 6, 7), None)

    def test_zero(self):
        self.assertEqual(modular_inverse([0], 1, 7), None)

    def test_empty_list(self):
        self.assertEqual(modular_inverse([], 1, 7), None)

    def test_invalid_N(self):
        self.assertEqual(modular_inverse([1], 0, 7), None)

    def test_invalid_P(self):
        self.assertEqual(modular_inverse([1], 1, 0), None)
