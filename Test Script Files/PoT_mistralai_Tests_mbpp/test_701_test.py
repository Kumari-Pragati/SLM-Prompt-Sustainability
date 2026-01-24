import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(equilibrium_index([3, 5, -9, 1, 3, 2]), 4)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), 4)
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), 0)

    def test_edge_case_empty(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_edge_case_single_element(self):
        self.assertEqual(equilibrium_index([0]), -1)

    def test_corner_case_all_zero(self):
        self.assertEqual(equilibrium_index([0, 0, 0]), 2)

    def test_corner_case_all_negative(self):
        self.assertEqual(equilibrium_index([-1, -2, -3]), -1)

    def test_corner_case_all_positive(self):
        self.assertEqual(equilibrium_index([1, 2, 3]), -1)
