import unittest
from mbpp_896_code import sort_list_last

class TestSortListLast(unittest.TestCase):

    def test_sort_list_last(self):
        self.assertEqual(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]), 
                         [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)])
        self.assertEqual(sort_list_last([(1, 7), (1, 3), (3, 4), (2, 5), (2, 6)]), 
                         [(2, 5), (2, 6), (1, 3), (1, 7), (3, 4)])
        self.assertEqual(sort_list_last([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]), 
                         [(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)])
