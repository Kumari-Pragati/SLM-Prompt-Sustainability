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
        self.assertEqual(get_inv_count([5, 1, 4, 2, 3], 5), 4)

    def test_duplicates_in_array(self):
        self.assertEqual(get_inv_count([1, 2, 2, 3, 3, 3], 6), 6)

    def test_array_with_negative_numbers(self):
        self.assertEqual(get_inv_count([-1, -2, -3, -4, -5], 5), 0)

    def test_array_with_negative_and_positive_numbers(self):
        self.assertEqual(get_inv_count([-1, 1, -2, 2, -3, 3], 6), 3)
