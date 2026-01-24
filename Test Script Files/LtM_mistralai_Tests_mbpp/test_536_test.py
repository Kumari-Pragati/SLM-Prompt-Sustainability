import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 1), [1, 4])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 2), [2, 4, 6])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 3), [3, 6])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 4), [4, 5])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 5), [5])

    def test_edge_and_boundary(self):
        self.assertEqual(nth_items([1], 1), [1])
        self.assertEqual(nth_items([1], 2), [])
        self.assertEqual(nth_items([], 1), [])
        self.assertEqual(nth_items([1], 0), [])

    def test_complex(self):
        self.assertEqual(nth_items([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [3, 6, 9])
        self.assertEqual(nth_items([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4), [4, 8])
        self.assertEqual(nth_items([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5), [5])
        self.assertEqual(nth_items([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6), [6, 12])
        self.assertEqual(nth_items([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 7), [7])
        self.assertEqual(nth_items([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8), [8])
        self.assertEqual(nth_items([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9), [9])
