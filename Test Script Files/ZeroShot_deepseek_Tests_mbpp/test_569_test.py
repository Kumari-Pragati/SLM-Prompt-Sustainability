import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_sort_sublists(self):
        self.assertEqual(sort_sublists([[3, 2, 1], [6, 5, 4], [9, 8, 7]]), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(sort_sublists([[10, 9, 8], [7, 6, 5], [4, 3, 2]]), [[8, 9, 10], [5, 6, 7], [2, 3, 4]])
        self.assertEqual(sort_sublists([[], [], []]), [[], [], []])
        self.assertEqual(sort_sublists([[1], [2], [3]]), [[1], [2], [3]])
        self.assertEqual(sort_sublists([]), [])
