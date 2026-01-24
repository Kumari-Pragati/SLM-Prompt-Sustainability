import unittest
from mbpp_701_code import equilibrium_index

class TestEquilibriumIndex(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5]), 2)
        self.assertEqual(equilibrium_index([1, 1, 1, 1, 1]), 0)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6]), 3)

    def test_edge(self):
        self.assertEqual(equilibrium_index([1]), 0)
        self.assertEqual(equilibrium_index([1, 1]), 0)
        self.assertEqual(equilibrium_index([1, 2, 3]), 0)
        self.assertEqual(equilibrium_index([1, 2, 3, 4]), -1)

    def test_complex(self):
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9]), 4)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4)
        self.assertEqual(equilibrium_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 4)
