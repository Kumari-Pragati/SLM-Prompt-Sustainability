import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):
    def test_positive_index(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 2), [2, 4])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 3), [3, 6])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 4), [4, 5])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 5), [5])

    def test_zero_index(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 0), [1])

    def test_negative_index(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], -1), [5, 4, 3, 2, 1])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], -2), [3, 5, 1])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], -3), [1, 4, 7])

    def test_empty_list(self):
        self.assertEqual(nth_items([], 2), [])

    def test_invalid_input(self):
        self.assertRaises(IndexError, lambda: nth_items([1, 2, 3], 0))
        self.assertRaises(TypeError, lambda: nth_items('abc', 2))
        self.assertRaises(TypeError, lambda: nth_items(123, 2))
