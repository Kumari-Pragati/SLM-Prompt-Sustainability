import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [1, 3, 5, 7, 9])

    def test_edge_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case2(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_edge_case3(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0), [])

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            nth_items([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -1)

    def test_empty_list(self):
        self.assertEqual(nth_items([], 1), [])

    def test_single_element_list(self):
        self.assertEqual(nth_items([1], 1), [1])
