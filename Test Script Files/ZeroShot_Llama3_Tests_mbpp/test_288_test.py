import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_modular_inverse(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 5, 7), 2)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5, 6], 6, 7), 3)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5, 6, 7], 7, 7), 1)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5, 6, 7, 8], 8, 9), 4)
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 10), 5)

    def test_modular_inverse_empty_array(self):
        self.assertEqual(modular_inverse([], 5, 7), 0)

    def test_modular_inverse_no_inverse(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11), 0)
