import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_single_item_list(self):
        self.assertEqual(sort_list_last([(1, 2)]), [(2, 1)])

    def test_multiple_items_list(self):
        self.assertEqual(sort_list_last([(3, 1), (2, 4), (1, 5)]), [(1, 5), (2, 4), (3, 1)])

    def test_mixed_types_list(self):
        self.assertEqual(sort_list_last([(3, 'a'), (2, 'b'), (1, 'c')]), [(1, 'c'), (2, 'b'), (3, 'a')])

    def test_duplicate_items_list(self):
        self.assertEqual(sort_list_last([(3, 1), (3, 2), (1, 5)]), [(1, 5), (3, 1), (3, 2)])

    def test_invalid_input_list(self):
        with self.assertRaises(TypeError):
            sort_list_last([1, 2])
