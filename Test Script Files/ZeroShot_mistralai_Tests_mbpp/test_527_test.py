import unittest
from mbpp_527_code import List

from 527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_pairs_count([], 0, 0), 0)

    def test_single_element(self):
        self.assertEqual(get_pairs_count([1], 1, 1), 0)
        self.assertEqual(get_pairs_count([1], 1, 2), 0)

    def test_two_elements(self):
        self.assertEqual(get_pairs_count([1, 2], 2, 3), 1)
        self.assertEqual(get_pairs_count([1, 2], 2, 4), 0)
        self.assertEqual(get_pairs_count([1, 2], 2, 1), 0)

    def test_multiple_elements(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 5), 2)
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 6), 3)
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 7), 0)
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 1), 0)
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 2), 2)
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 4), 3)
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 5), 2)
