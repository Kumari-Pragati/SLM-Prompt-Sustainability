import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_sublists([[2, 3], [1, 2]]), [[2, 3], [1, 2]])

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_boundary_case_single_sublist(self):
        self.assertEqual(sort_sublists([[1, 2]]), [[1, 2]])

    def test_corner_case_already_sorted_sublists(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_corner_case_reverse_sorted_sublists(self):
        self.assertEqual(sort_sublists([[2, 1], [4, 3]]), [[2, 1], [4, 3]])

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(sort_sublists([[2, 2], [1, 1]]), [[2, 2], [1, 1]])

    def test_corner_case_single_element_sublists(self):
        self.assertEqual(sort_sublists([[2], [1]]), [[2], [1]])

    def test_corner_case_empty_sublists(self):
        self.assertEqual(sort_sublists([[], []]), [[]])
