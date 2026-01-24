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
        self.assertEqual(get_inv_count([5, 2, 8, 3, 1], 5), 4)

    def test_reverse_sorted_array(self):
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5), 4)

    def test_duplicates(self):
        self.assertEqual(get_inv_count([1, 2, 2, 3, 3, 3], 6), 3)

    def test_edge_case(self):
        self.assertEqual(get_inv_count([1, 1, 1, 1, 1], 5), 0)
