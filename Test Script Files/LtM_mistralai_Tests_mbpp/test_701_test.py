import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(equilibrium_index([1, -1, 1]), 1)
        self.assertEqual(equilibrium_index([-1, 1, 1]), 2)
        self.assertEqual(equilibrium_index([-1, -1, 1, 1]), 3)

    def test_edge_and_boundary(self):
        self.assertEqual(equilibrium_index([0]), -1)
        self.assertEqual(equilibrium_index([1]), -1)
        self.assertEqual(equilibrium_index([-1]), -1)
        self.assertEqual(equilibrium_index([1, 0]), -1)
        self.assertEqual(equilibrium_index([-1, 0]), -1)

    def test_complex(self):
        self.assertEqual(equilibrium_index([3, 5, -9, 1, 3, 2]), 4)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), -1)
        self.assertEqual(equilibrium_index([-1, -2, -3, -4, -5]), -1)
