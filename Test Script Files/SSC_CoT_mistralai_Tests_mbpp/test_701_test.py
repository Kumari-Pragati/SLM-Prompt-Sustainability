import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(equilibrium_index([-1, 1, 2, -2, 1, -1, 0]), 3)
        self.assertEqual(equilibrium_index([-7, 2, 3, -6, 7, -4, 2, -1, 2, -3, 7]), 7)

    def test_edge_cases(self):
        self.assertEqual(equilibrium_index([0]), -1)
        self.assertEqual(equilibrium_index([1]), -1)
        self.assertEqual(equilibrium_index([-1]), -1)
        self.assertEqual(equilibrium_index([1, -1]), 0)
        self.assertEqual(equilibrium_index([-1, 1, -1]), -1)

    def test_empty_list(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_negative_numbers_only(self):
        self.assertEqual(equilibrium_index([-5, -3, -1]), -1)

    def test_positive_numbers_only(self):
        self.assertEqual(equilibrium_index([1, 3, 5]), -1)
