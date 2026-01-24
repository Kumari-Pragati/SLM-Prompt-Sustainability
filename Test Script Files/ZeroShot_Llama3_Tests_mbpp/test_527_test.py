import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_get_pairs_count(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 7), 2)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 9), 1)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 10), 0)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 6), 2)
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 5), 0)
        self.assertEqual(get_pairs_count([], 0, 0), 0)
        self.assertEqual(get_pairs_count([1], 1, 1), 0)
        self.assertEqual(get_pairs_count([1, 2], 2, 3), 1)
        self.assertEqual(get_pairs_count([1, 2, 3], 3, 4), 1)
