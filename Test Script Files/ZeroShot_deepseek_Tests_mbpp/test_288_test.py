import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 5), 1)
        self.assertEqual(modular_inverse([4, 5, 6], 3, 7), 2)
        self.assertEqual(modular_inverse([7, 8, 9], 3, 11), 1)

    def test_negative_numbers(self):
        self.assertEqual(modular_inverse([-1, -2, -3], 3, 5), 1)
        self.assertEqual(modular_inverse([-4, -5, -6], 3, 7), 2)
        self.assertEqual(modular_inverse([-7, -8, -9], 3, 11), 1)

    def test_zero(self):
        self.assertEqual(modular_inverse([0, 1, 2], 3, 5), 1)
        self.assertEqual(modular_inverse([0, -1, -2], 3, 7), 2)

    def test_large_numbers(self):
        self.assertEqual(modular_inverse([100, 200, 300], 3, 500), 1)
        self.assertEqual(modular_inverse([400, 500, 600], 3, 700), 2)

    def test_large_modulus(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 1000), 1)
        self.assertEqual(modular_inverse([4, 5, 6], 3, 2000), 2)
