import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):
    def test_sort_ascending(self):
        self.assertEqual(sort_list_last([(1, 2), (3, 4), (5, 6)]), [(1, 2), (3, 4), (5, 6)])

    def test_sort_descending(self):
        self.assertEqual(sort_list_last([(6, 5), (4, 3), (2, 1)]), [(6, 5), (4, 3), (2, 1)])

    def test_empty_list(self):
        self.assertEqual(sort_list_last([]), [])

    def test_single_item(self):
        self.assertEqual(sort_list_last([(1,)]), [(1,)])

    def test_mixed_ascending_and_descending(self):
        self.assertEqual(sort_list_last([(1, 2), (6, 5), (3, 4), (2, 1)]), [(1, 2), (3, 4), (6, 5), (2, 1)])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_list_last(123)
