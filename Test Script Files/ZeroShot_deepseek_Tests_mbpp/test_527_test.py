import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_get_pairs_count(self):
        self.assertEqual(get_pairs_count([1, 1, 1, 1], 4, 2), 6)
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 5), 2)
        self.assertEqual(get_pairs_count([1, 5, 7, 1], 4, 6), 1)
        self.assertEqual(get_pairs_count([0, 0, 0, 0], 4, 0), 6)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 5), 1)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 10), 4)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 15), 1)
        self.assertEqual(get_pairs_count([], 0, 10), 0)
