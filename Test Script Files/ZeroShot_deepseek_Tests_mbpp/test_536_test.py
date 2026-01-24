import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(nth_items([], 2), [])

    def test_single_item_list(self):
        self.assertEqual(nth_items([1], 2), [1])

    def test_multiple_items_list(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [3, 6, 9])

    def test_large_list(self):
        self.assertEqual(nth_items(list(range(1, 1001)), 10), list(range(10, 1001, 10)))

    def test_n_equals_1(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])

    def test_n_equals_0(self):
        with self.assertRaises(IndexError):
            nth_items([1, 2, 3, 4, 5], 0)

    def test_n_greater_than_list_length(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 6), [])
