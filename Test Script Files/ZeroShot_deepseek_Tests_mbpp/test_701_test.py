import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_equilibrium_index_exists(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), 3)

    def test_equilibrium_index_not_exists(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 6]), -1)

    def test_equilibrium_index_single_element(self):
        self.assertEqual(equilibrium_index([5]), 0)

    def test_equilibrium_index_empty_list(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_equilibrium_index_negative_numbers(self):
        self.assertEqual(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]), 3)
