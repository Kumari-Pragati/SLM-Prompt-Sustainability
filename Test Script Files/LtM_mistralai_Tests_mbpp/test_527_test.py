import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 5), 1)
        self.assertEqual(get_pairs_count([10, 15, 3, 7], 4, 17), 1)

    def test_edge_and_boundary(self):
        self.assertEqual(get_pairs_count([], 0, 1), 0)
        self.assertEqual(get_pairs_count([1], 1, 1), 0)
        self.assertEqual(get_pairs_count([1, 1], 2, 2), 1)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 6), 2)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 7), 0)

    def test_complex(self):
        self.assertEqual(get_pairs_count([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10, 6), 3)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 15), 5)
