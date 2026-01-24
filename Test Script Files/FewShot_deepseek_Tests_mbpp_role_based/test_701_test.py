import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(equilibrium_index([1]), 0)

    def test_boundary_case_empty_array(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_boundary_case_all_positive_numbers(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), -1)

    def test_boundary_case_all_negative_numbers(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), -1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            equilibrium_index("not an array")
