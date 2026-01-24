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
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 3), [3, 6, 9])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 4), [5])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 5), [1])

    def test_negative_step(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], -1), [5, 4, 3, 2, 1])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], -2), [3, 1])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], -3), [5, 2])
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], -4), [1])

    def test_zero_step(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 0), [])

    def test_list_with_duplicates(self):
        self.assertListEqual(nth_items([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 2), [1, 1, 3, 3, 5, 5])

    def test_list_with_long_step(self):
        self.assertListEqual(nth_items([1, 2, 3, 4, 5], 6), [])

    def test_list_with_negative_num(self):
        with self.assertRaises(ValueError):
            nth_items([1, 2, 3, 4, 5], -6)
