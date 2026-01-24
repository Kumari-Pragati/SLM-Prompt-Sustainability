import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(get_inv_count([1], 1), 0)

    def test_sorted_array(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5), 0)

    def test_unsorted_array(self):
        self.assertEqual(get_inv_count([5, 2, 8, 1, 4], 5), 4)

    def test_duplicates(self):
        self.assertEqual(get_inv_count([1, 2, 2, 3, 3, 3], 6), 3)

    def test_negative_numbers(self):
        self.assertEqual(get_inv_count([-1, -2, -3, -4, -5], 5), 0)

    def test_large_array(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 0)
