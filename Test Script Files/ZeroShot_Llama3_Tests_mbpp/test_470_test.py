import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_add_pairwise(self):
        self.assertEqual(add_pairwise((1, 2, 3)), (3, 4, 6))
        self.assertEqual(add_pairwise((1, 1, 1)), (2, 2, 2))
        self.assertEqual(add_pairwise((5, 5, 5)), (10, 10, 10))
        self.assertEqual(add_pairwise((-1, 1, 1)), (0, 2, 2))
        self.assertEqual(add_pairwise((0, 0, 0)), (0, 0, 0))
        self.assertEqual(add_pairwise((-1, -1, -1)), (-2, -2, -2))
        self.assertEqual(add_pairwise((1, 2, 3, 4, 5)), (3, 4, 6, 7, 8))
        self.assertEqual(add_pairwise((-1, -2, -3, -4, -5)), (-2, -4, -6, -8, -10))
