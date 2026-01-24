import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):
    def test_positive_n_typical_use_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 2), [2, 4])

    def test_zero_n_edge_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 0), [])

    def test_negative_n_edge_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], -1), [5, 3, 1])

    def test_empty_list_edge_case(self):
        self.assertEqual(nth_items([], 2), [])

    def test_list_with_one_item_edge_case(self):
        self.assertEqual(nth_items([1], 2), [])
