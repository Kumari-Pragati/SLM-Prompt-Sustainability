import unittest
from mbpp_536_code import nth_items

class TestNthItems(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 2), [1, 3, 5])

    def test_edge_case(self):
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5])
        self.assertEqual(nth_items([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_edge_case_negative(self):
        with self.assertRaises(IndexError):
            nth_items([1, 2, 3, 4, 5], 6)

    def test_empty_list(self):
        self.assertEqual(nth_items([], 2), [])

    def test_single_element_list(self):
        self.assertEqual(nth_items([1], 1), [1])

    def test_list_with_duplicates(self):
        self.assertEqual(nth_items([1, 2, 2, 3, 3, 3], 2), [1, 2, 3])
