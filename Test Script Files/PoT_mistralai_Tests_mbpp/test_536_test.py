import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 2), [2, 4])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 3), [3, 6, 9])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 4), [5])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 5), [1])

    def test_edge_case_n_1(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])

    def test_edge_case_empty_list(self):
        self.assertListEqual(nth_items([], 2), [])

    def test_edge_case_negative_n(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], -1), [5, 1, 2, 3, 4])

    def test_edge_case_zero_n(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 0), [])
