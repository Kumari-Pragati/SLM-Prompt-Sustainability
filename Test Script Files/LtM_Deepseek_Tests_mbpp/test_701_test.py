import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), -1)

    def test_equilibrium_index_exists(self):
        self.assertEqual(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]), 3)

    def test_empty_input(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_single_element_array(self):
        self.assertEqual(equilibrium_index([1]), -1)

    def test_negative_numbers(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -1]), 0)

    def test_large_numbers(self):
        self.assertEqual(equilibrium_index([1000000, -1000000, 0]), 1)
