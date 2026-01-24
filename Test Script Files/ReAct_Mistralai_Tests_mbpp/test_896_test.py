import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_sort_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_sort_single_item_list(self):
        self.assertEqual(sort_list_last([(1, 'a')]), [(1, 'a')])

    def test_sort_multiple_items_same_last(self):
        self.assertEqual(sort_list_last([(1, 'a'), (2, 'a'), (3, 'a'), (4, 'a')]), [(1, 'a'), (2, 'a'), (3, 'a'), (4, 'a')])

    def test_sort_multiple_items_different_last(self):
        self.assertEqual(sort_list_last([(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]), [(2, 'b'), (1, 'a'), (4, 'd'), (3, 'c')])

    def test_sort_mixed_types(self):
        self.assertEqual(sort_list_last([(1, 'a'), (2, 2), (3, 'c'), (4, 4)]), [(2, 2), (1, 'a'), (4, 4), (3, 'c')])

    def test_sort_none_last(self):
        with self.assertRaises(TypeError):
            sort_list_last([(1, None)])
