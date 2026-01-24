import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):
    def test_equilibrium_index_typical(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 3, 2, 1]), 3)

    def test_equilibrium_index_edge_case(self):
        self.assertEqual(equilibrium_index([1, 1, 1, 1, 1, 1, 1]), 0)

    def test_equilibrium_index_multiple_equilibrium(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]), 4)

    def test_equilibrium_index_no_equilibrium(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1)

    def test_equilibrium_index_empty_array(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_equilibrium_index_single_element_array(self):
        self.assertEqual(equilibrium_index([1]), -1)
