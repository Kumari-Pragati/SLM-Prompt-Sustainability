import unittest
from mbpp_104_code import sort_sublists

class TestSortSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4], [5, 6]]), [[(1, 2)], [(3, 4)], [(5, 6)]])

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_sublists([]), [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(sort_sublists([[1, 2]]), [[[(1, 2)]]])

    def test_edge_case_single_element_sublist(self):
        self.assertEqual(sort_sublists([[1, 2], [3, 4]]), [[[(1, 2)], (3, 4)]])

    def test_edge_case_sublist_with_duplicates(self):
        self.assertEqual(sort_sublists([[1, 2], [2, 3], [3, 4]]), [[[(1, 2)], (2, 3), (3, 4)]])

    def test_edge_case_sublist_with_duplicates_and_empty(self):
        self.assertEqual(sort_sublists([[1, 2], [2, 3], [3, 4], []]), [[[(1, 2)], (2, 3), (3, 4), []]])

    def test_edge_case_sublist_with_duplicates_and_empty_and_single_element(self):
        self.assertEqual(sort_sublists([[1, 2], [2, 3], [3, 4], [], [5, 6]]), [[[(1, 2)], (2, 3), (3, 4), [], [(5, 6)]]])
