import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_single_element(self):
        self.assertEqual(equilibrium_index([1]), -1)

    def test_negative_numbers(self):
        self.assertEqual(equilibrium_index([-1, -2, 3, 4]), -1)

    def test_positive_numbers(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4]), 2)

    def test_single_zero(self):
        self.assertEqual(equilibrium_index([0]), 0)

    def test_multiple_zeros(self):
        self.assertEqual(equilibrium_index([0, 0, 0]), 2)

    def test_multiple_equilibriums(self):
        self.assertEqual(equilibrium_index([1, -1, 1, -1]), 2)
