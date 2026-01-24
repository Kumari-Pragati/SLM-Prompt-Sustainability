import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6]), 3)

    def test_edge_case_zero_sum(self):
        self.assertEqual(equilibrium_index([1, -1, 1, -1, 1]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(equilibrium_index([1]), -1)

    def test_edge_case_all_positive(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), -1)

    def test_edge_case_all_negative(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), -1)

    def test_edge_case_all_equal(self):
        self.assertEqual(equilibrium_index([1, 1, 1, 1, 1]), -1)

    def test_edge_case_all_zero(self):
        self.assertEqual(equilibrium_index([0, 0, 0, 0, 0]), -1)

    def test_edge_case_empty_array(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_edge_case_single_element_zero(self):
        self.assertEqual(equilibrium_index([0]), -1)

    def test_edge_case_single_element_one(self):
        self.assertEqual(equilibrium_index([1]), -1)

    def test_edge_case_single_element_minus_one(self):
        self.assertEqual(equilibrium_index([-1]), -1)
