import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_single_sublist(self):
        self.assertEqual(sort_sublists([[1, 2, 3]]), [[1, 2, 3]])

    def test_multiple_sublists(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 
                         [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_sublists_of_tuples(self):
        self.assertEqual(sort_sublists([[(1, 2), (3, 4), (5, 6)], [(7, 8), (9, 10), (11, 12)]]), 
                         [[(1, 2), (3, 4), (5, 6)], [(7, 8), (9, 10), (11, 12)]])

    def test_sublists_of_tuples_with_duplicates(self):
        self.assertEqual(sort_sublists([[(1, 2), (3, 4), (5, 6), (5, 6)], [(7, 8), (9, 10), (11, 12)]]), 
                         [[(1, 2), (3, 4), (5, 6), (5, 6)], [(7, 8), (9, 10), (11, 12)]])

    def test_sublists_of_tuples_with_duplicates_and_empty(self):
        self.assertEqual(sort_sublists([[(1, 2), (3, 4), (5, 6), (5, 6), ()], [(7, 8), (9, 10), (11, 12)]]), 
                         [[(1, 2), (3, 4), (5, 6), (5, 6), ()], [(7, 8), (9, 10), (11, 12)]])
