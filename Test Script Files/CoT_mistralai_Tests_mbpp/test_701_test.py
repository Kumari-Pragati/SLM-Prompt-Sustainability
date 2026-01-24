import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_single_element(self):
        self.assertEqual(equilibrium_index([1]), -1)
        self.assertEqual(equilibrium_index([-1]), -1)

    def test_positive_list(self):
        self.assertEqual(equilibrium_index([-1, 1, -1]), 1)
        self.assertEqual(equilibrium_index([3, 5, -2, 2, -1, 7, 4]), 6)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), -1)

    def test_negative_list(self):
        self.assertEqual(equilibrium_index([-5, -2, -1, -4]), 0)
        self.assertEqual(equilibrium_index([-1, -2, -3, -4]), -1)

    def test_zero_sum_list(self):
        self.assertEqual(equilibrium_index([1, -1]), 1)
        self.assertEqual(equilibrium_index([-1, 1]), 0)
        self.assertEqual(equilibrium_index([-1, 1, -1, 1]), 2)

    def test_invalid_input(self):
        self.assertRaises(TypeError, equilibrium_index, 1.5)
        self.assertRaises(TypeError, equilibrium_index, (1, 2, 3))
