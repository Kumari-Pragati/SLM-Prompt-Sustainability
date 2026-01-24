import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_modular_inverse_simple_case(self):
        self.assertEqual(modular_inverse([2, 3, 4, 5], 6, 7), 4)

    def test_modular_inverse_edge_case(self):
        self.assertEqual(modular_inverse([0], 1, 7), 0)

    def test_modular_inverse_negative_case(self):
        self.assertEqual(modular_inverse([-1, -2, -3], 3, 5), 2)

    def test_modular_inverse_large_input(self):
        self.assertEqual(modular_inverse([1000000001, 1000000002, 1000000003], 3, 1000000007), 2)
