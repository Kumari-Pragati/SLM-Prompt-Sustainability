import unittest
from mbpp_569_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_sort_sublists(self):
        self.assertEqual(sort_sublists([[5,2,8],[4,6,3],[1,7,9]]), [[2,5,8],[3,4,6],[1,7,9]])
        self.assertEqual(sort_sublists([[-5,2,8],[4,6,3],[1,7,9]]), [[-5,2,8],[3,4,6],[1,7,9]])
        self.assertEqual(sort_sublists([[5,2,8],[4,6,3],[1,7,9],[10,9,8]]), [[2,5,8],[3,4,6],[1,7,9],[8,9,10]])
        self.assertEqual(sort_sublists([[]]), [[[]]])
        self.assertEqual(sort_sublists([[],[1,2,3]]), [[],[1,2,3]])
        self.assertEqual(sort_sublists([[1,2,3],[4,5,6]]), [[1,2,3],[4,5,6]])

    def test_sort_sublists_empty_list(self):
        self.assertEqual(sort_sublists([]), [])
