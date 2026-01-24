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

    def test_sublists_with_duplicates(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [3, 4, 5], [6, 7, 8]]), 
                         [[1, 2, 3], [3, 4, 5], [6, 7, 8]])

    def test_sublists_with_empty_sublist(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [], [4, 5, 6]]), 
                         [[1, 2, 3], [], [4, 5, 6]])
