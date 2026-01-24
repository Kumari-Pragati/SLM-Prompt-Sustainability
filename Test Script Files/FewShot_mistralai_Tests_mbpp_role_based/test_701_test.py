import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), 3)
        self.assertEqual(equilibrium_index([-1, 2, 3, 4, -5]), 3)
        self.assertEqual(equilibrium_index([1, 1, 1, 1, 1]), 4)
        self.assertEqual(equilibrium_index([0, 0, 0, 0, 0]), 4)

    def test_empty_list(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_single_element(self):
        self.assertEqual(equilibrium_index([1]), -1)

    def test_negative_numbers(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), -1)

    def test_zero(self):
        self.assertEqual(equilibrium_index([0]), -1)
        self.assertEqual(equilibrium_index([0, 0]), -1)
