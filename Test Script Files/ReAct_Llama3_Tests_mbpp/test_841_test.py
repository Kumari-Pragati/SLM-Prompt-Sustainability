import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_inv_count([5], 1), 0)

    def test_sorted_array(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5), 0)

    def test_unsorted_array(self):
        self.assertEqual(get_inv_count([5, 1, 3, 2, 4], 5), 3)

    def test_reverse_sorted_array(self):
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5), 4)

    def test_duplicates_in_array(self):
        self.assertEqual(get_inv_count([5, 5, 3, 2, 1], 5), 3)

    def test_array_with_duplicates_and_sorted(self):
        self.assertEqual(get_inv_count([5, 5, 3, 2, 1, 1], 6), 3)
