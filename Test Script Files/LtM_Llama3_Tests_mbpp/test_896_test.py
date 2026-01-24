import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_empty_input(self):
        self.assertEqual(sort_list_last([]), [])

    def test_single_element(self):
        self.assertEqual(sort_list_last([(1, 2)]), [(1, 2)])

    def test_multiple_elements(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4), (5, 6), (7, 8)]), [(1, 2), (3, 4), (5, 6), (7, 8)])

    def test_negative_numbers(self):
        self.assertEqual(sort_list_last([(-1, 2), (3, 4), (5, 6)]), [(-1, 2), (3, 4), (5, 6)])

    def test_duplicates(self):
        self.assertEqual(sort_list_last([(1, 2), (1, 3), (2, 4), (3, 5)]), [(1, 2), (1, 3), (2, 4), (3, 5)])
