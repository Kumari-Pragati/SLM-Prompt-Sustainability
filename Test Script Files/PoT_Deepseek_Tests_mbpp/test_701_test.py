import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]), 3)

    def test_empty_array(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_single_element_array(self):
        self.assertEqual(equilibrium_index([1]), -1)

    def test_all_positive_numbers(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), -1)

    def test_all_negative_numbers(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), -1)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(equilibrium_index([-1, 2, -3, 4, -5]), 3)

    def test_large_numbers(self):
        self.assertEqual(equilibrium_index([1000, 2000, 3000, 4000, 5000]), -1)

    def test_large_and_small_numbers(self):
        self.assertEqual(equilibrium_index([-1000, 2000, -3000, 4000, -5000]), 3)
