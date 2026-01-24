import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(get_pairs_count([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_pairs_count([1], 1, 1), 0)
        self.assertEqual(get_pairs_count([-1], 1, -1), 0)

    def test_simple_pair(self):
        self.assertEqual(get_pairs_count([1, 2], 2, 3), 1)
        self.assertEqual(get_pairs_count([-1, -2], 2, 1), 1)

    def test_multiple_pairs(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 5), 2)
        self.assertEqual(get_pairs_count([-1, -2, -3, -4], 4, 0), 2)

    def test_sum_greater_than_array_sum(self):
        self.assertEqual(get_pairs_count([1, 2, 3], 3, 4), 0)
        self.assertEqual(get_pairs_count([-1, -2, -3], 3, 0), 0)

    def test_sum_less_than_array_min(self):
        self.assertEqual(get_pairs_count([1, 2, 3], 3, -1), 0)
        self.assertEqual(get_pairs_count([-1, -2, -3], 3, -4), 0)
