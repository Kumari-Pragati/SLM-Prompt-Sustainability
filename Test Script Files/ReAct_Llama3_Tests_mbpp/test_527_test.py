import unittest
from mbpp_527_code import get_pairs_count

class TestGetPairsCount(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(get_pairs_count([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_pairs_count([1], 1, 2), 0)

    def test_no_pairs_found(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 5), 0)

    def test_pairs_found(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4], 4, 3), 1)

    def test_pairs_found_with_duplicates(self):
        self.assertEqual(get_pairs_count([1, 2, 2, 3, 3], 5, 4), 2)

    def test_sum_in_array(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 7), 2)

    def test_sum_not_in_array(self):
        self.assertEqual(get_pairs_count([1, 2, 3, 4, 5], 5, 10), 0)
