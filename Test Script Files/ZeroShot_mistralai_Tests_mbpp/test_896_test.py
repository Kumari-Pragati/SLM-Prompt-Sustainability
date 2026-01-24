import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_single_item_list(self):
        self.assertEqual(sort_list_last([(1, 'a')]), [(1, 'a')])

    def test_multiple_items_list(self):
        self.assertEqual(sort_list_last([(2, 'b'), (1, 'a'), (3, 'c')]), [(3, 'c'), (2, 'b'), (1, 'a')])

    def test_duplicate_items_list(self):
        self.assertEqual(sort_list_last([(2, 'b'), (1, 'a'), (2, 'b'), (3, 'c')]), [(3, 'c'), (2, 'b'), (2, 'b'), (1, 'a')])

    def test_negative_numbers(self):
        self.assertEqual(sort_list_last([(-1, 'a'), (0, 'b'), (-2, 'c')]), [(-2, 'c'), (-1, 'a'), (0, 'b')])

    def test_mixed_types(self):
        self.assertEqual(sort_list_last([(1, 'a'), (2, 3), (3, 'b')]), [(3, 'b'), (2, 3), (1, 'a')])
