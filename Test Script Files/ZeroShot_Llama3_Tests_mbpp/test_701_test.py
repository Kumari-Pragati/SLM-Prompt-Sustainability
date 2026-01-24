import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_equilibrium_index(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(equilibrium_index([-7, 1, 5, 2, -4, 3, 2, 3]), 3)
        self.assertEqual(equilibrium_index([8, 3, -1, 2, -1, 6]), 3)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), -1)
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5, -6]), -1)
