import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(nth_items([], 3), [])

    def test_single_item_list(self):
        self.assertListEqual(nth_items([1], 1), [1])
        self.assertListEqual(nth_items([1], 2), [])
        self.assertListEqual(nth_items([1], 3), [1])

    def test_simple_list(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 2), [2, 4])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 3), [3, 6])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 4), [4, 7])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 5), [5])

    def test_negative_n(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], -1), [5, 4, 3, 2, 1])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], -2), [4, 2])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], -3), [3, 6])

    def test_zero_n(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 0), [])
