import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(equilibrium_index([]), -1)

    def test_single_element(self):
        self.assertEqual(equilibrium_index([1]), -1)
        self.assertEqual(equilibrium_index([-1]), -1)

    def test_positive_only(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), 3)
        self.assertEqual(equilibrium_index([10, 20, 30, 40, 50]), 4)

    def test_negative_only(self):
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), 4)
        self.assertEqual(equilibrium_index([-10, -20, -30, -40, -50]), 0)

    def test_mixed_positive_and_negative(self):
        self.assertEqual(equilibrium_index([1, -2, 3, -4, 5]), 3)
        self.assertEqual(equilibrium_index([-1, 2, -3, 4, -5]), 4)

    def test_zero_sum(self):
        self.assertEqual(equilibrium_index([0, 0, 0]), 1)
        self.assertEqual(equilibrium_index([-1, 1, -1, 1]), 2)

    def test_negative_sum(self):
        self.assertEqual(equilibrium_index([-1, -2, -3]), -1)

    def test_large_input(self):
        arr = [i for i in range(1000)]
        self.assertNotEqual(equilibrium_index(arr), -1)
