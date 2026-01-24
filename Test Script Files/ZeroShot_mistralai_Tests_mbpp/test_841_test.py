import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_inv_count([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(get_inv_count([1], 1), 0)

    def test_sorted_list(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4], 4), 0)

    def test_unsorted_list(self):
        self.assertEqual(get_inv_count([6, 3, 1, 4, 5], 5), 5)

    def test_negative_numbers(self):
        self.assertEqual(get_inv_count([-1, -2, -3, 0, 1], 5), 4)

    def test_duplicates(self):
        self.assertEqual(get_inv_count([1, 1, 2, 3], 4), 2)
