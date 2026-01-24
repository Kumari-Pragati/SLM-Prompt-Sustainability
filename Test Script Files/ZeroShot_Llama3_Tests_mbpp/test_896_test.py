import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_sort_list_last(self):
        self.assertEqual(sort_list_last([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), [(7, 8, 9), (4, 5, 6), (1, 2, 3)])
        self.assertEqual(sort_list_last([(9, 8, 7), (6, 5, 4), (3, 2, 1)]), [(9, 8, 7), (6, 5, 4), (3, 2, 1)])
        self.assertEqual(sort_list_last([(1, 2, 3), (1, 2, 3), (1, 2, 3)]), [(1, 2, 3), (1, 2, 3), (1, 2, 3)])
        self.assertEqual(sort_list_last([]), [])
        self.assertEqual(sort_list_last([(1, 2, 3)]), [(1, 2, 3)])

    def test_sort_list_last_edge_cases(self):
        self.assertEqual(sort_list_last([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]), [(10, 11, 12), (7, 8, 9), (4, 5, 6), (1, 2, 3)])
        self.assertEqual(sort_list_last([(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)]), [(13, 14, 15), (10, 11, 12), (7, 8, 9), (4, 5, 6), (1, 2, 3)])
