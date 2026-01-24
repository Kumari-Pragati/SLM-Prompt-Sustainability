import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 2), [1, 3, 5])

    def test_empty_list(self):
        self.assertEqual(nth_items([], 2), [])

    def test_single_item_list(self):
        self.assertEqual(nth_items([1], 2), [])

    def test_large_step(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), [1, 6])

    def test_negative_step(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], -2), [])

    def test_zero_step(self):
        with self.assertRaises(IndexError):
            nth_items([1, 2, 3, 4, 5], 0)

    def test_large_step_with_negative_values(self):
        self.assertEqual(nth_items([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5), [10, 5])
