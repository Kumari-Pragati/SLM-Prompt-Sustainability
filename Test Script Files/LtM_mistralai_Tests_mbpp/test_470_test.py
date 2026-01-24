import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4)), (3, 5, 6))
        self.assertEqual(add_pairwise((5, 6, 7, 8)), (11, 12, 13))

    def test_edge_cases(self):
        self.assertEqual(add_pairwise((1, 2)), (3,))
        self.assertEqual(add_pairwise((1, 2, 3)), (4, 2))
        self.assertEqual(add_pairwise((1, 2, 3, 4, 5)), (6, 7, 8))

    def test_complex(self):
        self.assertEqual(add_pairwise((1, -2, 3, -4)), (2, 1, 7, -3))
        self.assertEqual(add_pairwise((-1, 2, -3, 4)), (-3, 4, -1, 8))
        self.assertEqual(add_pairwise((-1, -2, -3, -4)), (3, 2, 1, -7))
