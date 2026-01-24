import unittest
from mbpp_288_code import modular_inverse

class TestModularInverse(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 5, 7), 1)

    def test_edge_case(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 5, 1), 0)

    def test_edge_case2(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 5, 5), 1)

    def test_edge_case3(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 0, 7), 0)

    def test_edge_case4(self):
        self.assertEqual(modular_inverse([], 5, 7), 0)

    def test_edge_case5(self):
        self.assertEqual(modular_inverse([1, 2, 3, 4, 5], 5, 0), 0)
