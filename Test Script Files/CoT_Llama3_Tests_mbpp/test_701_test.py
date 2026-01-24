import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):
    def test_equilibrium_index(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(equilibrium_index([-1, -2, 3, -4, 5]), 2)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), -1)
        self.assertEqual(equilibrium_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 0)
        self.assertEqual(equilibrium_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]), -1)
        self.assertEqual(equilibrium_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1]), 0)
        self.assertEqual(equilibrium_index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 0)
