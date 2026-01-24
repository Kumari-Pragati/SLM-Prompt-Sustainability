import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]), 3)

    def test_edge_case_single_element(self):
        self.assertEqual(equilibrium_index([5]), 0)

    def test_edge_case_empty_array(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_corner_case_all_positive(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), -1)

    def test_corner_case_all_negative(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), -1)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            equilibrium_index("not an array")

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            equilibrium_index(None)
