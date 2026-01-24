import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):
    def test_equilibrium_index_positive(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), 2)

    def test_equilibrium_index_negative(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), 0)

    def test_equilibrium_index_zero(self):
        self.assertEqual(equilibrium_index([0, 0, 0, 0, 0]), 0)

    def test_equilibrium_index_single_element(self):
        self.assertEqual(equilibrium_index([1]), 0)

    def test_equilibrium_index_no_equilibrium(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4]), -1)

    def test_equilibrium_index_empty_list(self):
        self.assertEqual(equilibrium_index([]), -1)
