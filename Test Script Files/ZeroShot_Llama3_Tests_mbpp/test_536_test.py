import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_nth_items(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [1, 3, 5, 7, 9])
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [1, 4, 7, 10])
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), [1, 5, 9, 10])
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), [1, 10])
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11), [])
