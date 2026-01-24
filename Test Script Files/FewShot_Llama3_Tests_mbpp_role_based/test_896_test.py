import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_list_last([(1,)]), [(1,)])

    def test_multiple_elements_list(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4), (5, 6)]), [(6, 5), (4, 3), (2, 1)])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_list_last([(1, 2), (2, 3), (3, 4)]), [(4, 3), (3, 2), (2, 1)])

    def test_list_with_negative_numbers(self):
        self.assertEqual(sort_list_last([(-1, -2), (-3, -4), (-5, -6)]), [(-6, -5), (-4, -3), (-2, -1)])
