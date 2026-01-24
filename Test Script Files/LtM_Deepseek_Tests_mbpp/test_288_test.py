import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 5), 1)
        self.assertEqual(modular_inverse([4, 5, 6], 3, 7), 1)

    def test_edge_conditions(self):
        self.assertEqual(modular_inverse([], 0, 10), 0)
        self.assertEqual(modular_inverse([1, 2, 3], 3, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(modular_inverse([1, 2, 3], 3, 2), 0)
        self.assertEqual(modular_inverse([1, 2, 3], 3, 3), 1)
        self.assertEqual(modular_inverse([1, 2, 3], 3, 4), 1)

    def test_complex_cases(self):
        self.assertEqual(modular_inverse([1, 4, 9], 3, 10), 1)
        self.assertEqual(modular_inverse([1, 4, 9], 3, 11), 1)
        self.assertEqual(modular_inverse([1, 4, 9], 3, 12), 1)
