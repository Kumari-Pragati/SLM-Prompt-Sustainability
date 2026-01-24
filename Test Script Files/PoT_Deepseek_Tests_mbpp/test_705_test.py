import unittest
from mbpp_705_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[1, 2], [3, 4], [5, 6]])

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_boundary_case_single_sublist(self):
        self.assertEqual(sort_sublists([[1, 2, 3]]), [[1, 2, 3]])

    def test_corner_case_duplicate_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [1, 2]]), [[1, 2], [1, 2]])

    def test_typical_case_with_longer_sublists(self):
        self.assertEqual(sort_sublists([[1, 2, 3], [4, 5], [6]]), [[6], [4, 5], [1, 2, 3]])

    def test_edge_case_with_empty_sublists(self):
        self.assertEqual(sort_sublists([[], [1, 2], []]), [[], [1, 2], []])
